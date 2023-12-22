 -- 创建索引

-- CREATE INDEX beijing_geom_gist ON beijing USING gist(geom)

-- CREATE INDEX idx_beijing_img_location_longitude_latitude ON beijing_img_location (longitude, latitude);

-- ceate table xx as
Create Table beijing_img_poi AS
SELECT
  i.img_key,
  --p.osm_id,
  p.id,
  --ST_X(p.geom) AS poi_longitude,
  --ST_Y(p.geom) AS poi_latitude,
  ST_Distance(p.geom::geography, ST_MakePoint(CAST(i.longitude AS double precision), CAST(i.latitude AS double precision))::geography) AS distance
FROM
  beijing_img_location i,
  beijing p
WHERE
  ST_DWithin(p.geom::geography, ST_MakePoint(CAST(i.longitude AS double precision), CAST(i.latitude AS double precision))::geography, 500)
ORDER BY
  ST_Distance(p.geom::geography, ST_MakePoint(CAST(i.longitude AS double precision), CAST(i.latitude AS double precision))::geography) ASC
LIMIT 5;