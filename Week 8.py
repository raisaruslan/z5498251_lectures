import tk_utils

import pandas as pd
import numpy as np

from datetime import datetime
import datetime as dt #--> module in python called datetime


#dt.datetime --> class<datetime.datetime>
#type(datetime.datetime) --> class 'type'
dt_now = dt.datetime.now() #-called at 2024-10-29 12:46:50
print(type(dt_now))
print(dt_now) #dt_now is an instance of datetime.datetime
# Output = 2024-10-29 12:46:50.232222
print(repr(dt_now)) #suggest how to create datetime.datetime instances
# Output = datetime.datetime(2024, 10, 29, 12, 51, 41, 513485)

#Create datetime.datetime instances

d= dt.datetime(
    year=2024,
    month=12,
    day=22,
    minute=12,
    second=22,
    microsecond=373737,
    )

str(d)
repr(d)

d = dt.datetime(year=2024, month=12, day=22)
d.strftime('%b %d, %Y')

#Create timedelta object
elapsed = dt.timedelta(days=1, hours=8)
#we have

#Use the datetime.datetime and datetime.timedelta classes,
#1. For how many seconds have you been alive?
#2. How old will you be in 1340 days?

from datetime import datetime, timedelta

birth_date = datetime(2000, 12, 22)
current_date = datetime.now()

time_alive = current_date - birth_date
seconds_alive = time_alive.total_seconds()
print("You have been alive for about", int(seconds_alive), "seconds.")

days_ahead = 1340
future_date = current_date + timedelta(days=days_ahead)

age_in_1340_days = future_date.year - birth_date.year

if (future_date.month, future_date.day) < (birth_date.month, birth_date.day):
    age_in_1340_days -= 1

print("In 1,340 days, you will be", age_in_1340_days, "years old.")
