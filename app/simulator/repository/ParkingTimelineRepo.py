from database import *

class ParkingTimelineRepo:
    def __init__(self, db_connection):
      self.connection: PostgresConnection = db_connection
    
    # Create a new parking record
    def create(self, osm_id, parking_type, capacity, occupied, update_time):
      query = """
      INSERT INTO parking_timeline (osm_id, parking_type, capacity, occupied, update_time)
      VALUES (%(osm_id)s, %(parking_type)s, %(capacity)s, %(occupied)s, %(update_time)s);
      """
      params = {
        'osm_id': osm_id, 
        'parking_type': parking_type,
        'capacity': capacity,
        'occupied': occupied,
        'update_time': update_time
      }
      self.__execute(query, params)

    # Read parking records
    def find_by_id(self, osm_id: int) -> list|int|None:
      query = "SELECT * FROM parking_timeline WHERE osm_id = %(osm_id)s;"
      params = {'osm_id': osm_id}
      return self.__execute(query, params)
          

    # Update a parking record
    def update(self, osm_id, parking_type, capacity, occupied, update_time):
      query = """
      UPDATE parking_timeline
      SET parking_type = %(parking_type)s, 
          capacity = %(capacity)s, 
          occupied = %(occupied)s, 
          update_time = %(update_time)s
      WHERE osm_id = %(osm_id)s;
      """
      params = {
        'osm_id': osm_id, 
        'parking_type': parking_type,
        'capacity': capacity,
        'occupied': occupied,
        'update_time': update_time
      }
      self.__execute(query, params)

    # Delete a parking record
    def delete(self, osm_id):
      query = "DELETE FROM parking_timeline WHERE osm_id = %(osm_id)s;"
      params = {'osm_id': osm_id}
      return self.__execute(query,params)

    # Special method to update 'occupied' field and 'update_time'
    def update_status(self, osm_id, occupied, update_time):
      query = """
      UPDATE parking_timeline
      SET occupied = %(occupied)s, 
          update_time = %(update_time)s
      WHERE osm_id = %(osm_id)s;
      """
      params = {
        'osm_id': osm_id, 
        'occupied': occupied,
        'update_time': update_time
      }
      self.__execute(query, params)

    def __execute(self, query: str, params: dict|list = None) -> list|int|None :
      return self.connection.execute_query(query, params)
