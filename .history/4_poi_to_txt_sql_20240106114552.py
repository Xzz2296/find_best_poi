#!/usr/bin/env python
# coding: utf-8

# # 数据载入

# In[1]:


import pandas as pd
import os
from collections import Counter
import numpy as np
from tqdm import tqdm
import torch


# In[2]:
pd.set_option('display.max_colwidth', -1)

# In[3]:
poi_path =r'E:\xpj\research\POI\psqlcsv\rio.csv'
poi_prompt_path =r'E:\xpj\research\POI\result\rio_poi_prompt.xlsx'
image_path = r'E:\xpj\research\POI\psqlcsv\rio_img_location.csv'
image_poi_path = r'E:\xpj\research\POI\psqlcsv\rio_img_poi.csv'
desc_path =r'E:\xpj\research\POI\desc_merge\rio_desc_merged.csv'
best_poi_path = r'E:\xpj\research\POI\result\rio_best_poi.xlsx'
desc_poi_path = r'E:\xpj\research\POI\result\rio_desc_poi.xlsx'


# ## poi数据（全面）

# In[4]:
poi_data = pd.read_csv(poi_path,encoding='utf-8')
poi_df = pd.DataFrame(poi_data)
pic_data = pd.read_csv(image_path,encoding='utf-8')
pic_df = pd.DataFrame(pic_data)

# ## 照片poi关联

# In[10]:
pic_poi_data = pd.read_csv(image_poi_path,encoding='utf-8')
pic_poi_df = pd.DataFrame(pic_poi_data)
desc_pd =pd.read_csv(desc_path,encoding='utf-8')
poi_df_nec=poi_df.loc[:,['id', 'name', 'barrier', 'highway', 'address', 'place', 'man_made', 'other_tags']]


# In[14]:
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
# 加载BERT模型和分词器
tokenizer = AutoTokenizer.from_pretrained(r"E:\xpj\models\bert-base-uncased")
model = AutoModel.from_pretrained(r"E:\xpj\models\bert-base-uncased")
# In[15]:


# 定义计算相似度的函数
def calc_similarity(s1, s2):
    # 对句子进行分词，并添加特殊标记
    inputs = tokenizer([s1, s2], return_tensors='pt', padding=True, truncation=True)
    # 将输入传递给BERT模型，并获取输出
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state[:, 0, :].cpu().numpy()

    # 计算余弦相似度，并返回结果
    sim = np.dot(embeddings[0], embeddings[1]) / (np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1]))
    return sim
# In[16]:

def isEnglish(s):
    if isinstance(s, str):
        return s.isascii()
    return False
# 从txt中读取tag_list
tag_ignore_list = []
with open(r'E:\xpj\research\POI\tag_ignore_list.txt', 'r') as f:
    for line in f.readlines():
        tag_ignore_list.append(line.strip())
# print(tag_ignore_list)

def genSent(x):
    tags = None
    b = True    
    # sen = "The imformation of this point contains that "
    sen = "Nearby,"
    for key in ['name','barrier', 'highway','address','place','man_made']:
        if isinstance(x[key],str) and not isEnglish(x[key]):
            continue
        if not x[key].isna().iloc[0]:
            # print(x[key])
            sen = sen + key +" is " + x[key].iloc[0] + ","
    # print(sen)
    if not x['other_tags'].isna().iloc[0]:
        tags = x['other_tags'].iloc[0].split("\",\"")
        for tag in tags:
            try:
                tag = tag.replace("\"","")
                t = tag.split("=>")[0]
                k = tag.split("=>")[1]
                # 北京保留中文
                if not isEnglish(k) or not isEnglish(t):
                    print(k,t)
                    continue
                if list(t)[-1] == "=":
                    continue
                if t in tag_ignore_list:
                    continue
                sen = sen + t +" is " + k + ","
            except:
                pass    
    return sen

def store_poi(x):
    poi = x[0]    
    poi_im = poi_df_nec.loc[poi_df_nec['id']==poi]
    sen = genSent(poi_im)
    return sen

# In[18]:

result =[]
for index, row in tqdm(poi_df_nec.iterrows(), total=poi_df_nec.shape[0], desc="Processing"):
    result.append(store_poi(row))


poi_df_nec['poi_prompt'] = result
poi_df_nec.to_excel(poi_prompt_path)

def find_best_poi(x):
    # print(x)
    img_key = x['img_key']
    # img_file = img_key+'.jpg'
    img_file =img_key
    try:
        img_desc = desc_pd.loc[desc_pd['key']==img_file]['prompt'].iloc[0]
    except:
        print("The description of picture " + img_file +" doesn't exist")
        return  None,None
    pois = x[1::2]
    pois_dis =x[2::2]
    # print(pois)
    similarities = []
    sentences = []
    for index,poi in enumerate(pois):
        # 设置距离阈值
        if pois_dis[index] is not None and pois_dis[index]<100:

            # # 根据id从poi_df_nec中找到poi_prompt
            try:
                sen = poi_df_nec.loc[poi_df_nec['id']==poi]['poi_prompt'].iloc[0]
            except Exception as e:
                print(e)
                print("The poi_prompt of poi " + poi +" doesn't exist")
                continue
                   
            similarity = calc_similarity(img_desc,sen)
            sentences.append(sen)
            similarities.append(similarity)
        
    if len(similarities) == 0:
        best_poi=None
        return best_poi,0
    elif similarities and max(similarities)>0.5:
        best_poi = pois[similarities.index(max(similarities))]
        return best_poi,max(similarities)


# In[25]:


result = []
for _, row in tqdm(pic_poi_df.iterrows(), total=pic_poi_df.shape[0], desc="Processing"):
    result.append(find_best_poi(row))

result_df = pd.DataFrame(result,columns=['best_poi','best_poi_score']) # 将列表转换成DataFrame
pic_poi_df = pic_poi_df.join(result_df) # 将新的DataFrame添加到原始DataFrame中
# pic_poi_df.shape[0]

pic_poi_df.to_excel(best_poi_path)
df1 = pd.merge(pic_poi_df, poi_df_nec, left_on="best_poi",right_on = 'id',how="left")




def connect(x):
    image_file_name = x[0]
    image_name =image_file_name.split('.')[0]
    best_poi_row = df1.loc[df1['img_key']==image_name]['best_poi']
    best_poi = None
    if best_poi_row.notna().any():
        best_poi=int(best_poi_row.iloc[0])
        poi_prompt = poi_df_nec.loc[poi_df_nec['id']==best_poi]['poi_prompt'].iloc[0]
        return poi_prompt


# In[34]:

result2 = desc_pd.apply(lambda x: connect(x), axis=1,result_type='expand')
desc_pd['poi_prompt'] = result2
desc_pd.to_excel(desc_poi_path)

