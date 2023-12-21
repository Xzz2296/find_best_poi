CREATE TABLE beijing_img_poi AS
SELECT
  img_key,
  MAX(CASE WHEN rn = 1 THEN id END) AS id1,
  MAX(CASE WHEN rn = 1 THEN distance END) AS distance1,
  MAX(CASE WHEN rn = 2 THEN id END) AS id2,
  MAX(CASE WHEN rn = 2 THEN distance END) AS distance2,
  MAX(CASE WHEN rn = 3 THEN id END) AS id3,
  MAX(CASE WHEN rn = 3 THEN distance END) AS distance3,
  MAX(CASE WHEN rn = 4 THEN id END) AS id4,
  MAX(CASE WHEN rn = 4 THEN distance END) AS distance4,
  MAX(CASE WHEN rn = 5 THEN id END) AS id5,
  MAX(CASE WHEN rn = 5 THEN distance END) AS distance5
FROM (
  SELECT
    i.img_key,
    p.id,
    ST_Distance(p.geom::geography, ST_MakePoint(CAST(i.longitude AS double precision), CAST(i.latitude AS double precision))::geography) AS distance,
    ROW_NUMBER() OVER(PARTITION BY i.img_key ORDER BY ST_Distance(p.geom::geography, ST_MakePoint(CAST(i.longitude AS double precision), CAST(i.latitude AS double precision))::geography)) AS rn
  FROM
    beijing_img_location i,
    beijing p
  WHERE
    ST_DWithin(p.geom::geography, ST_MakePoint(CAST(i.longitude AS double precision), CAST(i.latitude AS double precision))::geography, 500)
) t
GROUP BY img_key;

ALTER TABLE beijing_img_poi ADD PRIMARY KEY (img_key);