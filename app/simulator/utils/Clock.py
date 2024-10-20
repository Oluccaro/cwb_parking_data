from datetime import datetime, timedelta

class Clock:
    def __init__(self, initial_time="2024-01-01 00:00:00", time_format="%Y-%m-%d %H:%M:%S"):
        """
        Initializes the clock with an initial formatted date and time.
        :param initial_time: A string representing the initial date and time.
        :param time_format: The format of the date and time string (default is "%Y-%m-%d %H:%M:%S").
        """
        self.time_format = time_format
        self.time = datetime.strptime(initial_time, self.time_format)

    def simulate(self, step_seconds=1, duration_steps=10):
        """
        Simulates the passage of time and returns an iterable.
        :param step_seconds: The number of seconds to advance in each step (default is 1 second).
        :param duration_steps: The total number of steps to simulate (default is 10 steps).
        :return: A generator that yields the current time at each step.
        """
        step = timedelta(seconds=step_seconds)
        for _ in range(duration_steps):
            self.time += step
            yield self.time.strftime(self.time_format)
    
    def reset(self, new_time="2024-01-01 00:00:00"):
        """
        Resets the clock to a new time.
        :param new_time: A string representing the new date and time.
        """
        self.time = datetime.strptime(new_time, self.time_format)

    def get_time(self):
        """
        Returns the current time as a string in the specified format.
        """
        return self.time.strftime(self.time_format)
    
    def get_day_of_week(self):
        """
        Returns the current day of the week as a string.
        Example: 'Monday', 'Tuesday', etc.
        """
        return self.time.strftime("%A")
    
    def get_hour_of_day(self):
        """
        Returns the current hour of the day (0-23).
        """
        return self.time.hour
