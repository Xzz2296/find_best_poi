import pandas as pd

def split_excel(file_path, num_parts):
    # 读取Excel文件
    df = pd.read_excel(file_path)

    # 计算每一部分的大小
    part_size = len(df) // num_parts

    # 分割数据并保存到新的Excel文件中
    for i in range(num_parts):
        start = i * part_size
        end = (i + 1) * part_size if i < num_parts - 1 else None
        part_df = df.iloc[start:end]
        part_df.to_excel(f'part_{i+1}.xlsx', index=False)

# 使用函数
split_excel('your_excel_file.xlsx', 5)