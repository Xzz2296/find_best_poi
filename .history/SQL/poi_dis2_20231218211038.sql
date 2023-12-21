CREATE TABLE beijing_img_poi AS
SELECT
  img_key,
  id,
  distance
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
WHERE rn <= 5;