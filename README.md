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

# 🐍 Python Development Environment with Docker

This setup allows you to develop and test Python code inside a Docker container. You can run specific scripts, install new Python modules, and ensure consistency across environments.

## 🚀 Getting Started

### Prerequisites 📋
- 🐳 [Docker](https://docs.docker.com/get-docker/)
- 🛠️ [Docker Compose](https://docs.docker.com/compose/install/)

### Setup 🔧

1. **Clone this repository** (or create your project directory).
2. **Build the Docker container:**

   ```bash
   docker-compose build
   ```

3. **Start the Docker container:**

   ```bash
   docker-compose up -d
   ```

### 🏃 Running Python Scripts

To execute a Python script inside the container, use the provided `runpy.sh` script. This allows you to run any Python script without attaching to the container manually.

```bash
./runpy.sh path/to/your_script.py
```

For example:

```bash
./runpy.sh scripts/my_script.py
```

### 🧪 Installing Python Modules

You have two options for installing Python packages: temporary (for testing) and permanent (added to the project).

#### Temporary Module Installation ⏳

To install a new module inside the container for testing, first, attach to the running container:

```bash
docker exec -it app-python-1 bash
```

Then, inside the container, use `pip` to install the required module:

```bash
pip install <module_name>
```

Or you can run direcly with this:

```bash
docker exec -it app-python-1 pip install <module-name>
```

#### Permanent Module Installation 📦

To permanently add a Python module to your project:

1. Open the `requirements.txt` file.
2. Add the desired module and version to the file. For example:

   ```text
   numpy==1.23.4
   scipy==1.10.1
   ```

3. Rebuild the container to install the new packages:

   ```bash
   docker-compose build
   ```

4. Restart the container:

   ```bash
   docker-compose up -d
   ```

5. **TIP**: You can check the modules you have install by running 
    ```bash
    pip list
    ```

    After that you can copy and paste the line of the new module you want and put it into the `requirements.txt`


### 🛑 Stopping the Container

To stop the container when you're done:

```bash
docker-compose down
```

### 📝 Summary of Commands

- **🛠️ Build and start the container:**

  ```bash
  docker-compose build
  docker-compose up -d
  ```

- **🏃 Run a Python script:**

  ```bash
  ./runpy.sh path/to/your_script.py
  ```

- **🔧 Install a new Python module temporarily (for testing):**

  ```bash
  docker exec -it app-python-1 bash
  pip install <module_name>
  ```

- **📦 Install a new Python module permanently (added to `requirements.txt`):**

  1. Add the module to `requirements.txt`.
  2. Rebuild the container:

     ```bash
     docker-compose build
     ```

  3. Restart the container:

     ```bash
     docker-compose up -d
     ```

- **🛑 Stop the container:**

  ```bash
  docker-compose down
  ```

---
