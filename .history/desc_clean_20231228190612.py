import pandas as pd
from tqdm import tqdm
# Read the data
file_path = r'E:\xpj\research\POI\desc_Google\chennai_desc.csv'
clean_path = r'E:\xpj\research\POI\desc_Google\chennai_desc_clean.xlsx'
df = pd.read_csv(file_path)
# 新建一个excel文件，用于存储清洗后的数据
df.to_excel(clean_path, index=False)
# data.to_csv(clean_path, index=False, encoding='utf-8')
# 读取csv文件
data = pd.read_excel(clean_path)
# 新建一个列，用于存储key
data['key'] = ''

# 读取文件名
files = data['image']
# 得到了一个数组，对每个文件进行处理
for file in tqdm(files, desc='正在处理', total=len(files)):
    try:
        key =file.split('_')[0]
    except Exception as e:
        continue
    # key = key_and_jw.split('_')[0]
    # print(key)
    # 将key写回到csv 对应的行中
    data.loc[data['image'] == file, 'key'] = key
    

print("操作完成！")