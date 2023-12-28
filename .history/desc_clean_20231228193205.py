import pandas as pd
from tqdm import tqdm
# Read the data
file_path = r'E:\xpj\research\POI\desc_Google\chennai_desc.csv'
clean_path = r'E:\xpj\research\POI\desc_Google\chennai_desc_clean.csv'
df = pd.read_csv(file_path)

# 新建一个列，用于存储key
df['key'] = None

# 读取文件名
files = df['image']

for file in tqdm(files, desc='正在处理', total=len(files)):
    try:
        key =file.split('_')[0]
        df.loc[df['image'] == file, 'key'] = key
    except Exception as e:
        continue
# 保存文件
df.to_csv(clean_path, columns=['key','prompt'] ,index=False)
    

print("操作完成！")