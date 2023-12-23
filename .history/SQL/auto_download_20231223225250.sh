#!/bin/bash

# 获取所有的表名
tables=$(psql -U svail -d svaildb -t -c "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

# 对每个表名执行\copy命令
for table in $tables; do
    psql -U your_username -d your_database -c "\copy (SELECT * FROM $table) TO '/workspace/xpj/csv_result/$table.csv' WITH CSV HEADER"
done