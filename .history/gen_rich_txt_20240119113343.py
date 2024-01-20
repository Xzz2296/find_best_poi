import pandas as pd
import os
from tqdm import tqdm  # 导入tqdm模块

# 读取Excel文件
excel_file = r'E:\xpj\research\POI\summary_result\beijing_summary_output.csv'  # 替换成你的Excel文件路径
df = pd.read_csv(excel_file)


# 获取总行数
total_rows = len(df)

# 指定保存文件的目录
output_directory = r'E:\xpj\research\POI\prompt_text\beijing'  # 替换成你想要保存文件的目录路径

# 使用tqdm显示进度
for index, row in tqdm(df.iterrows(), total=total_rows, desc="生成.txt文件进度"):
    file_name = os.path.splitext(row['key'])[0] + '.txt'  # 去掉扩展名并添加.txt扩展名
    if file_name =="#NAME?.txt" :
        continue
    # text = (str(row['prompt']) if pd.notna(row['prompt']) else '')
    rich_info ="This region is rich."
    text = (str(row['summary']) if pd.notna(row['summary']) else '')
    # text = (str(row['poi_prompt']) if pd.notna(row['poi_prompt']) else '') +'.' +(str(row['prompt']) if pd.notna(row['prompt']) else '')

    # text = row['prompt']+row['poi_prompt']  # 获取文本内容

    # 创建并写入txt文件
    file_path = os.path.join(output_directory, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

print("生成.txt文件完成。")
