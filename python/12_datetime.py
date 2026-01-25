
### Date time ###

"""
    datetime module to handle date and time
"""

# Getting datetime information
from datetime import datetime, date
now = datetime.now() # show current years month day hour minute and second
show_day = now.day
show_month = now.month
show_year = now.year
show_hour = now.hour
show_minute = now.minute
show_second = now.second
timestamp = now.timestamp()

today = datetime.today() # similar to now

# Sort date with format
print(f'{show_day}/{show_month}/{show_year}')
print(f'{show_hour}:{show_minute}:{show_second}')
print('timestamp', timestamp)

# Date and Data Format. There are many, here are some examples

# strftime
current_day = now.strftime('%Y-%m-%d %H:%M:%S')
print(f'Current day is: {show_day}/{show_month}/{show_year}')
print(current_day)
print(now)

# strptime
# The strptime() method creates a datetime object from the given string.
# The string needs to be in a certain format.
date_string = "24 January, 2026"
print("date_string =", date_string)
print("type of date_string =", type(date_string))
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
print("type of date_object =", type(date_object))

# Difference between two time
# Using 'date'
new_year = date(year=2027, month=1, day=1)
current_year = date(year=2026, month=1, day=24)
diff_years = new_year - current_year
print('There are ',diff_years,' until the new year')

# Using timedelta
from datetime import timedelta
time_delta = timedelta
time_one = time_delta(days=365, weeks=10)
time_two = time_delta(days=365, weeks=10)
# allows operations with dates
operation_sum = time_one - time_two
operation_sum = time_one + time_two
print(operation_sum)