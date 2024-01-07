import csv
import psycopg2

# 打开文件并读取列名
with open('E:\\xpj\\research\\POI\\psqlcsv\\kolkata_img_location.sql', 'r') as f:
    reader = csv.reader(f)
    columns = next(reader)

# 创建数据库连接
conn = psycopg2.connect(database="postgres", user="postgres", password="2014220336", host="localhost", port="5432")

# 创建一个游标对象
cur = conn.cursor()

# 创建COPY命令
copy_sql = f"""
COPY tablename({', '.join(columns)})
FROM 'E:\\xpj\\research\\POI\\psqlcsv\\kolkata_img_location.sql' 
WITH (FORMAT csv, HEADER true, DELIMITER ',');
"""

# 执行COPY命令
cur.execute(copy_sql)

# 提交事务
conn.commit()

# 关闭连接
cur.close()
conn.close()