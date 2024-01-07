import pandas as pd
import os

def split_excel(file_path, num_parts, output_dir):
    # 读取Excel文件
    df = pd.read_excel(file_path)

    # 计算每一部分的大小
    part_size = len(df) // num_parts

    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 分割数据并保存到新的Excel文件中
    for i in range(num_parts):
        start = i * part_size
        end = (i + 1) * part_size if i < num_parts - 1 else None
        part_df = df.iloc[start:end]
        output_path = os.path.join(output_dir, f'part_{i+1}.xlsx')
        part_df.to_excel(output_path, index=False)

# 使用函数
excel_file = r'E:\xpj\research\POI\result\bangkok_desc_poi.xlsx'  # 替换成你的Excel文件路径
split_excel(excel_file, 5, 'split_output')