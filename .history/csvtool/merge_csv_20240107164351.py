import os
import pandas as pd

# #读取两个CSV文件
# df1 = pd.read_csv(r'E:\xpj\research\POI\desc_Google\malindi_desc_clean.csv')
# df2 = pd.read_csv(r'E:\xpj\research\POI\desc_clean\Malindi_img_desc_clean.csv')

# # 合并两个DataFrame
# df = pd.concat([df1, df2])

# # 保存合并后的DataFrame
# df.to_csv(r'E:\xpj\research\POI\desc_merge\malindi_desc_merged.csv', index=False)
# print("操作完成！")


---------------------
#合并所有的csv文件

# 设置目录和输出文件名
directory = r'E:\xpj\research\POI\desc_Map\jans\jans'
output_file = r'E:\xpj\research\POI\desc_Map\Johannesburg_img_desc.csv'

# 获取目录下所有 CSV 文件列表
csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

# 读取并合并 CSV 文件
dfs = [pd.read_csv(os.path.join(directory, file)) for file in csv_files]
merged_df = pd.concat(dfs, ignore_index=True)

# 将合并后的 DataFrame 写入新的 CSV 文件
merged_df.to_csv(output_file, index=False)
