import pandas

# Read the data
data = pandas.read_csv(r'E:\xpj\research\POI\desc_Google\chennai_desc.csv')
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