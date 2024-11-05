import tk_utils
tk_utils.sync_dbox()


import datetime as dt #--> module in python called datetime
from datetime import datetime

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

#Q1
birthdate = datetime(2000, 12, 22)
current_time = datetime.now()
time_alive = current_time - birthdate
how_many_seconds = time_alive.total_seconds()

#Q2
future_age = 1340
future_date = current_time + timedelta(future_age)
age_in_1340_days = future_age.year - birthdate.year

#We can use pandas.to_datetime to modify columns in a DF
#dtype of df.loc[:, 'date']
#df.loc[:, 'date'
