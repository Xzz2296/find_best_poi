#!/bin/bash
tables=$(psql -U svail -d svaildb -t -c "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
for table in $tables; do
    if [[ "$table" != *geodb* && "$table" != *meta_info* ]]; then
        psql -U svail -d svaildb -c "\copy (SELECT * FROM $table) TO '/workspace/xpj/csv_result/$table.csv' WITH CSV HEADER"
    fi
done