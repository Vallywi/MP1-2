# Exercise 24 - Units of Time

sec_per_minute = 60
sec_per_hour = 3600
sec_per_day = 86400 

num_days = int(input("Enter number of days: "))
num_hours = int(input("Enter number of hours: "))
num_minutes = int(input("Enter number of minutes: "))
num_seconds = int(input("Enter number of seconds: "))

def calculate():
    totalSeconds = (num_days * sec_per_day) + (num_hours * sec_per_hour) + (num_minutes * sec_per_minute) + num_seconds
    return totalSeconds

totalSeconds = calculate()

print(f"The total duration in seconds is {totalSeconds} seconds")
