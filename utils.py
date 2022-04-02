import seaborn
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime
from sklearn.preprocessing import LabelEncoder

def is_high_season(row):
    now_date = datetime.strptime(row['Fecha-I'],'%Y-%m-%d %H:%M:%S').date()

    if (now_date >= pd.to_datetime('2017-12-15') and now_date <= pd.to_datetime('2017-12-31'))\
    or (now_date >= pd.to_datetime('2017-01-01') and now_date <= pd.to_datetime('2017-03-03'))\
    or (now_date >= pd.to_datetime('2017-07-15') and now_date <= pd.to_datetime('2017-07-31'))\
    or (now_date >= pd.to_datetime('2017-09-11') and now_date <= pd.to_datetime('2017-09-30')):
        return 1
    else:
        return 0

def flight_delay(row):
    # This function gets the difference between two dates and then convert the result to minutes.
    return (datetime.strptime(row['Fecha-O'],'%Y-%m-%d %H:%M:%S') - datetime.strptime(row['Fecha-I'],'%Y-%m-%d %H:%M:%S')).total_seconds()/ 60

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

def pie_plot(df):
    inner_circle = plt.Circle( (0,0), 0.7, color='white')
    plt.figure(figsize=(20,10))
    plt.rcParams['axes.labelsize'] = 20
    seaborn.set(font_scale = 2)
    plt.rcParams['text.color'] = 'black'
    plt.rcParams['font.size'] = 20
    plt.pie(df['atraso_15'].value_counts()/len(df), labels =df['atraso_15'].value_counts().index, autopct='%.0f%%',
            wedgeprops = { 'linewidth' : 5, 'edgecolor' : 'white' })
    p = plt.gcf()
    p.gca().add_artist(inner_circle)

    return plt.show()

def stack_plot(df):
    fig = plt.figure(figsize=(20, 20))
    seaborn.displot(data=df, y='OPERA', hue="atraso_15", multiple="stack", height=12,aspect=2, stat='density')
    plt.tick_params(labelrotation=0)
    plt.title('Proportion of on-time and dealyed flights per Airline')

    return plt.show()

def dump_data(df, path):
    colums_to_dump =['temporada_alta', 'dif_min', 'atraso_15', 'periodo_dia']
    df[colums_to_dump].to_csv(path)
