import pandas as pd
from sqlalchemy import create_engine

# 读取CSV文件
df = pd.read_csv('E:\\xpj\\research\\POI\\psqlcsv\\chennai.csv')

# 创建数据库连接
engine = create_engine('postgresql://postgres:2014220336@localhost:5432/postgres')

# 将数据写入数据库
df.to_sql('chennai', engine, if_exists='append', index=False)