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
-- 查看shell 脚本 通俗易懂

--删除table
--drop table malindi_img_poi

--查询
--select *
--from kolkata_img_location
-- where img_key is not NULL

-- 复制table
-- Create table mombasa_img_location_copy AS
-- select *
-- from mombasa_img_location

-- 合并两个键，将第二列的值合并到第一列为空的行
--UPDATE mombasa_img_location
--SET img_key = COALESCE(img_key, img_id);
--SET longitude = COALESCE(longitude, lon);
--SET latitude = COALESCE(latitude, lat);

