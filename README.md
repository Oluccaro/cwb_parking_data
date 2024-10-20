---

# 🚀 Starting the Setup

## Step 1: Start the PostGIS Instance and `osm2pgsql` Image
To begin, start the necessary services by running the following command:

```bash
docker compose up -d
```

The data we’ll be using is located in the `map.osm` file, which contains information about a small region from Curitiba.

---

## Step 2: Import the Data

Navigate to the `/data` folder and make the `run_import.sh` script executable:

```bash
chmod +x run_import.sh
```

Now you can run the import script:

```bash
./run_import.sh <file_name>
```

- **Note:** The `<file_name>` argument is optional. If you specify it, the script will import the data from that file in the `/map-data` directory. If omitted, it will default to importing `map.osm`.

Alternatively, you can run the following command directly from your terminal (while inside the `/data` directory):

```bash
docker compose run -v $(pwd)/map-data:/data osm2pgsql \
  -d osm \    
  -U osmuser \
  -H postgis \
  -P 5432 \             
  -c -k /data/map.osm
```

---

## Expected Output

If everything works correctly, you should see output similar to this:

```
2024-10-07 07:07:08  All postprocessing on table 'planet_osm_point' done in 0s.
2024-10-07 07:07:08  All postprocessing on table 'planet_osm_line' done in 0s.
2024-10-07 07:07:08  All postprocessing on table 'planet_osm_polygon' done in 0s.
2024-10-07 07:07:08  All postprocessing on table 'planet_osm_roads' done in 0s.
2024-10-07 07:07:08  Storing properties to table '"public"."osm2pgsql_properties"'.
2024-10-07 07:07:08  osm2pgsql took 0s overall.
```

---

## Step 3: Access the PostgreSQL Database

Once the import is done, you can access the PostgreSQL database running in Docker using the username and password you’ve configured. Feel free to use your preferred method to connect.

---

## Example Query to Test

Here’s a SQL query you can run to test the imported data:

```sql
-- Replace 'StreetName' with the name of the street you're interested in
SELECT p.*
FROM planet_osm_polygon p
JOIN planet_osm_roads r
  ON r.name = 'Rua Conselheiro Laurindo' -- Replace with the actual street name
WHERE ST_DWithin(r.way, p.way, 120)      -- 120 meters buffer zone around the road
AND p.amenity = 'parking'                -- only parking polygons
AND p.tags->'parking' = 'street_side';   -- only street-side parking
```

Feel free to download new datasets to further test the setup.

---
