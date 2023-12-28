import pandas

# Read the data
data = pandas.read_csv(r'E:\xpj\research\POI\desc_Google\chennai_desc.csv')
# 读取文件名
files = data['image']
# 得到了一个数组，对每个文件进行处理
for file in files:
    key =file.split('_')[0]
    # key = key_and_jw.split('_')[0]
    print(file)


print("hello world")