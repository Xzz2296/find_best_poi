 -- 创建索引

-- CREATE INDEX beijing_geom_gist ON beijing USING gist(geom)

-- CREATE INDEX idx_beijing_img_location_longitude_latitude ON beijing_img_location (longitude, latitude);
-- CREATE INDEX idx_img_key_location_karachi ON karachi_img_location (img_key);
-- ceate table xx as

-- table改名
-- alter table beijing_img_location rename to beijing_img_location_bak;
-- 下载table到本地csv 需要进入psql命令行，连接41服务器即可
-- psql -U svail svaildb
-- \copy (select * from delhi_img_poi) to '/workspace/xpj/delhi_img_poi.csv' with csv header

--下载所有表到本地
-- psql -U svail svaildb
-- 获取所有表名
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';  -- 如果你的表在 'public' 模式中


DO $$ 
DECLARE 
    table_name text;
BEGIN
    FOR table_name IN (SELECT table_name FROM information_schema.tables WHERE table_schema = 'public') LOOP
        EXECUTE format('\COPY (SELECT * FROM %I) TO ''//workspace/xpj/csv_result/%I.csv'' WITH CSV HEADER', table_name, table_name);
    END LOOP;
END $$;

