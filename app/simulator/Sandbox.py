#This is a place to put tests ans example of usage of code

from utils import *
from database import *
import datetime as dt

# clock = Clock(initial_time="2012-10-01 12:00:00")  # Set initial time to October 1st, 2024 at noon

# for current_time in clock.simulate(step_seconds=3600, duration_steps=24*30):  # Simulate 5 hours
#     print(f"Simulated time: {current_time}")
#     print(f"Day of the week: {clock.get_day_of_week()}")
#     print(f"Hour of the day: {clock.get_hour_of_day()}")
    

# traffic = Traffic()

# central_traffic = traffic.get_normalized_curitiba_cetral_traffic()
# periferical_traffic = traffic.get_normalized_curitiba_periferical_traffic()

# for row in central_traffic:
#   print(row)
  
# for row in periferical_traffic:
#   print(row)
  

    
# # Example usage:

# # Example for boolean probability
# print(f"Probability True: {Probability.probability_true(50) * 100:.2f}%")
# print(f"Probability False: {Probability.probability_false(10) * 100:.2f}%")

# # Example for normal distribution
# mean = 100
# std_dev = 20
# x_value = 100

# prob = Probability(mean, std_dev)

# print(f"Normal distribution value at {x_value}: {prob.normal_distribution(x_value):.4f}")
# print(f"Percentage below {x_value}: {prob.percentage_below_value(x_value)*100:.2f}%")
# print(f"Percentage above {x_value}: {prob.percentage_above_value(x_value)*100:.2f}%")
# print(f"Percentage between (with 5% window) {x_value}: {prob.percentage_around_value(x_value, 5)*100:.2f}%")


# # Example usage Holidays
# holidays = Holidays()
# print(holidays.list_feriados)

# feriado = dt.datetime.strptime("2024-11-15", "%Y-%m-%d")
# nao_feriado = dt.datetime.strptime("2024-10-15", "%Y-%m-%d")
# print(holidays.is_holiday(feriado))
# print(holidays.is_holiday(nao_feriado))

##Example of use

db = ConnectionResolver().get()
query = """
SELECT p.*
FROM planet_osm_polygon p
JOIN planet_osm_roads r
  ON r.name = 'Rua Conselheiro Laurindo' -- Replace 'StreetName' with the actual name of the street
WHERE ST_DWithin(r.way, p.way, 120)      -- 10 meters buffer zone around the road
and p.amenity = 'parking'                -- only parking polygons
and p.tags->'parking' = 'street_side'    -- only on street parking
"""
result = db.execute_query(query)
print(result)


