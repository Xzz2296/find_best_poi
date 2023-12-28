import pandas as pd

# 读取两个CSV文件
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')

# 合并两个DataFrame
df = pd.concat([df1, df2])

# 保存合并后的DataFrame
df.to_csv('merged.csv', index=False)