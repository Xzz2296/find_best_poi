import pandas

# Read the data
data = pandas.read_csv(r'E:\xpj\research\POI\desc\chennai_desc.csv')
# 读取文件名
files = data['image']
# 得到了一个数组，对每个文件进行处理
for file in files:
    key_and_jw =file.split('.')[0]
    print(file)


print("hello world")