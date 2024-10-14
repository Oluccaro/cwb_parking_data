# Example usage
from Clock import Clock
from Traffic import Traffic

clock = Clock(initial_time="2012-10-01 12:00:00")  # Set initial time to October 1st, 2024 at noon

for current_time in clock.simulate(step_seconds=3600, duration_steps=24*30):  # Simulate 5 hours
    print(f"Simulated time: {current_time}")
    print(f"Day of the week: {clock.get_day_of_week()}")
    print(f"Hour of the day: {clock.get_hour_of_day()}")
    

traffic = Traffic()

central_traffic = traffic.get_normalized_curitiba_cetral_traffic()
periferical_traffic = traffic.get_normalized_curitiba_periferical_traffic()

for row in central_traffic:
  print(row)
  
for row in periferical_traffic:
  print(row)