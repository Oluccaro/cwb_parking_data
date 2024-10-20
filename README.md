# Starting the setup

## Start the postgis instance and osm2pgsql image by running
```bash
docker compose up -d
```

The data we're going to  be using is on map.osm and consist about a small region from Curitiba

To do the import of the data you just run (while inside de /data directory)

```bash
 docker compose run -v $(pwd)/map-data:/data osm2pgsql \
 -d osm \    
 -U osmuser \
 -H postgis \
 -P 5432 \             
-c -k /data/map.osm
```

You're supposed to see this at the end of the process:

```
2024-10-07 07:07:08  All postprocessing on table 'planet_osm_point' done in 0s.
2024-10-07 07:07:08  All postprocessing on table 'planet_osm_line' done in 0s.
2024-10-07 07:07:08  All postprocessing on table 'planet_osm_polygon' done in 0s.
2024-10-07 07:07:08  All postprocessing on table 'planet_osm_roads' done in 0s.
2024-10-07 07:07:08  Storing properties to table '"public"."osm2pgsql_properties"'.
2024-10-07 07:07:08  osm2pgsql took 0s overall.
```

After that you can access the postgres database that is running on docker the way you prefer with username and password you configure :D

### Query example to test

```sql
-- Replace 'StreetName' with the name of the street you're interested in
SELECT p.*
FROM planet_osm_polygon p
JOIN planet_osm_roads r
  ON r.name = 'Rua Conselheiro Laurindo' -- Replace 'StreetName' with the actual name of the street
WHERE ST_DWithin(r.way, p.way, 120)      -- 10 meters buffer zone around the road
AND p.amenity = 'parking'                -- only parking polygons
AND p.tags->'parking' = 'street_side'    -- only on street parking
```

You can download new sets of data to test it
