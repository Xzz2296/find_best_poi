import pandas as pd
from tqdm import tqdm
# Read the data
file_path = r'E:\xpj\research\POI\desc_Google\capetown_desc.csv'
clean_path = r'E:\xpj\research\POI\desc_Google\capetown_desc_clean.csv'
df = pd.read_csv(file_path,encoding='utf-8')

# 新建一个列，用于存储key
df['key'] = None

# 读取文件名
files = df['image']

for file in tqdm(files, desc='正在处理', total=len(files)):
    try:
        # key =file.split('_')[0]
        # 返回从左到右第一个'_'的位置
        # index = file.index('_')
        # # 如果'_'的下一位是数字，则返回'_'的位置
        # if file[index+1].isdigit():
        key = file[:22]
        df.loc[df['image'] == file, 'key'] = key
    except Exception as e:
        continue
# 保存文件
df.to_csv(clean_path, columns=['key','prompt'] ,index=False)
    

print("操作完成！")