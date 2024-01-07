import psycopg2

# 创建数据库连接
conn = psycopg2.connect(database="postgres", user="postgres", password="2014220336", host="localhost", port="5432")

# 创建一个游标对象
cur = conn.cursor()

# 打开SQL文件
f = open('E:\\xpj\\research\\POI\\psqlcsv\\kolkata_img_location.sql', 'r')

# 执行SQL文件
cur.execute(f.read())

# 提交事务
conn.commit()

# 关闭连接
cur.close()
conn.close()