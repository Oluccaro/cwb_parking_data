#!/bin/bash
set -e

# Create user and database
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER osmuser WITH PASSWORD 'osmpass';
    CREATE DATABASE osm WITH OWNER osmuser ENCODING 'UTF8';
EOSQL

# Enable PostGIS and HStore extensions
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname=osm <<-EOSQL
    CREATE EXTENSION postgis;
    CREATE EXTENSION hstore;
EOSQL
