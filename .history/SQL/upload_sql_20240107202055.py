import psycopg2

# 创建数据库连接
conn = psycopg2.connect(database="postgres", user="postgres", password="2014220336", host="localhost", port="5432")

# 创建一个游标对象
cur = conn.cursor()

# 打开SQL文件
with open('E:\\xpj\\research\\POI\\psqlcsv\\kolkata_img_location.sql', 'r') as f:
    sql_file = f.read()

# 分割SQL文件为单独的SQL语句
sql_commands = sql_file.split(';')

# 逐一执行每个SQL语句
for command in sql_commands:
    if command.strip() != '':
        cur.execute(command)

# 提交事务
conn.commit()

# 关闭连接
cur.close()
conn.close()