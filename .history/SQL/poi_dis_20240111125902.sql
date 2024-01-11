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

--\copy (select * from kolkata_img_poi) to 'E:\xpj\research\POI\psqlcsv\kolkata_img_poi.csv' with csv header

-- 上传csv到服务器
-- psql -U postgres postgres
-- COPY kolkata FROM 'E:\xpj\research\POI\psqlcsv\kolkata.csv' WITH (FORMAT CSV, HEADER true, DELIMITER ',');

--导出sql文件 shell中执行
--pg_dump -U username -d database -t table -f table.sql

--导入sql文件 psql命令行中执行
--psql -U username -d database -f table.sql


--下载所有表到本地
-- psql -U svail svaildb
-- 查看服务器上的shell 脚本 

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


-- CREATE TABLE kolkata_img_location (
--     id integer NOT NULL,
--     geom geometry(Point,4326),
--     captured_a character varying(24),
--     camera_mak character varying(254),
--     created_at character varying(24),
--     sequences_ character varying(254),
--     pano integer,
--     user_key character varying(254),
--     username character varying(254),
--     img_key character varying(254),
--     ca numeric,
--     longitude character varying(254),
--     latitude character varying(254),
--     loongiude character varying(254),
--     img_id character varying(254),
--     lon character varying(254),
--     lat character varying(254),
--     layer character varying(254),
--     path character varying(254)
-- );


CREATE TABLE public.kolkata (
    id integer NOT NULL,
    geom public.geometry(Point,4326),
    osm_id character varying(254),
    name character varying(254),
    barrier character varying(254),
    highway character varying(254),
    ref character varying(254),
    address character varying(254),
    is_in character varying(254),
    place character varying(254),
    man_made character varying(254),
    other_tags character varying(254)
);
