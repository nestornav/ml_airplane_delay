import pandas as pd

from datetime import datetime


def is_high_season(row):
    now_date = datetime.strptime(row['Fecha-I'],'%Y-%m-%d %H:%M:%S').date()

    if (now_date >= pd.to_datetime('2017-12-15') and now_date <= pd.to_datetime('2017-03-03'))\
    or (now_date >= pd.to_datetime('2017-07-15') and now_date <= pd.to_datetime('2017-07-31'))\
    or (now_date >= pd.to_datetime('2017-09-11') and now_date <= pd.to_datetime('2017-09-30')):
        return 1
    else:
        return 0

def flight_delay(row):
    # This function gets the difference between two dates and then convert the result to minutes.
    return (datetime.strptime(row['Fecha-O'],'%Y-%m-%d %H:%M:%S') - datetime.strptime(row['Fecha-I'],'%Y-%m-%d %H:%M:%S')).total_seconds()/ 60.0

def has_delay(row):
    # If dif_min is grater than 15 inutes we will asign 1 otherwise 0
    return 1 if row['dif_min'] > 15 else 0

def get_day_period(row):
    now_time = datetime.strptime(row['Fecha-I'],'%Y-%m-%d %H:%M:%S').time()

    if now_time >= datetime.strptime('5:00:00','%H:%M:%S').time() and now_time <= datetime.strptime('11:59:00','%H:%M:%S').time():
        return 'maniana'
    elif now_time >= datetime.strptime('12:00:00','%H:%M:%S').time() and now_time <= datetime.strptime('18:59:00','%H:%M:%S').time():
        return 'tarde'
    elif (now_time >= datetime.strptime('19:00:00','%H:%M:%S').time() and now_time <= datetime.strptime('23:59:00','%H:%M:%S').time()) or\
         (now_time >= datetime.strptime('00:00:00','%H:%M:%S').time() and now_time <= datetime.strptime('04:59:00','%H:%M:%S').time()):
        return 'noche'
