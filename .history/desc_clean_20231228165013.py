import pandas

# Read the data
file_path = r'E:\xpj\research\POI\desc_Google\chennai_desc.csv'
clean_path = r'E:\xpj\research\POI\desc_Google\chennai_desc_clean.csv'
data = pandas.read_csv(file_path)
# 新建一个csv文件，用于存储清洗后的数据
data.to_csv(clean_path, index=False, encoding='utf-8')
# 读取csv文件
data = pandas.read_csv(clean_path, encoding='utf-8')
# 新建一个列，用于存储key
data['key'] = ''

# 读取文件名
files = data['image']
# 得到了一个数组，对每个文件进行处理
for file in files:
    try:
        key =file.split('_')[0]
    except Exception as e:
        continue
    # key = key_and_jw.split('_')[0]
    # print(key)
    # 将key写回到csv 对应的行中
    data.loc[data['image'] == file, 'key'] = key
    


print("hello world")