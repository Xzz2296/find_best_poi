import psycopg2

# 创建数据库连接
conn = psycopg2.connect(database="postgres", user="postgres", password="2014220336", host="localhost", port="5432")

# 创建一个游标对象
cur = conn.cursor()

# 执行COPY命令
copy_sql = """
COPY tablename(column1, column2, column3, ...)
FROM 'E:\\xpj\\research\\POI\\psqlcsv\\kolkata_img_location.sql' 
WITH (FORMAT csv, HEADER true, DELIMITER ',');
"""
cur.execute(copy_sql)

# 提交事务
conn.commit()

# 关闭连接
cur.close()
conn.close()