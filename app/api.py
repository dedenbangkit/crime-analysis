#1 DR Number            11 Victim Age           22 Crime Description
#2 Date Reported        12 Victim Sex           23 Crime Code 1
#3 Date Occurred        13 Victim Descent       24 Crime Code 2
#4 Time Occurred        14 Premise Code         25 Crime Code 3
#5 Area ID              15 Premise Description  26 Crime Code 4
#6 Area Name            16 Weapon Used Code     27 Address
#7 Reporting District   17 Weapon Description   28 Cross Street
#8 Crime Code           18 Status Code          29 Location
#9 Crime Description    20 Status Description
#10 MO Codes            21 Crime Code

import pandas as pd
from app.settings import setting
source = pd.read_csv(setting['file'],skiprows=1,header=None,nrows=setting['limit']);

def field(x, y):
    src = source[x]
    data = src.rename(columns = setting['vars'])
    data = data.groupby(y).size().to_frame(name = 'count').reset_index()
    items = []
    for i in range(len(data)):
        obj = {}
        for name in y:
            obj.update({name:data[name][i]})
        items.append(obj)
    return items

def db():
    src = source[setting['source']]
    src['lat'] = pd.DataFrame(src[25].str.replace('(','').str.replace(')','').str.split(', ').str[0])
    src['lng'] = pd.DataFrame(src[25].str.replace('(','').str.replace(')','').str.split(', ').str[1])
    data = src.rename(columns = setting['vars'])
    data[['lat','lng']] = data[['lat','lng']].apply(pd.to_numeric)
    data['date_occured'] = pd.to_datetime(source[2])
    data['date_reported'] = pd.to_datetime(source[1])
    data.drop('location', axis=1, inplace=True)
    response = data.to_json(orient='records')
    return response
