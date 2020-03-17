# 3.1 How many seconds are in an hour?
minute = 60
hour = 60
seconds_per_hour = minute * hour

print(seconds_per_hour, "seconds per hour")

# 3.2 How many seconds are in a day? 
day = 24
seconds_per_day = seconds_per_hour * 24
print(seconds_per_day, "seconds per day")

# 3.3 Divide seconds_per_day by seconds_per_hour
print (seconds_per_day / seconds_per_hour, "hours per day (floating-point division (/))")
print (seconds_per_day // seconds_per_hour, "hours per day (integer division (//))")