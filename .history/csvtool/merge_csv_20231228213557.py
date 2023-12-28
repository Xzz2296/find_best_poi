import pandas as pd

# 读取两个CSV文件
df1 = pd.read_csv(r'E:\xpj\research\POI\chennai_desc_clean.csv')
df2 = pd.read_csv(r'E:\xpj\research\POI\desc_clean\Chennai_img_desc_clean.csv')

# 合并两个DataFrame
df = pd.concat([df1, df2])

# 保存合并后的DataFrame
df.to_csv(r'E:\xpj\research\POI\desc_merge\chennai_desc_merged.csv', index=False)
print("操作完成！")