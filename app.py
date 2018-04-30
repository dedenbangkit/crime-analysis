
#DR Number,Date Reported,Date Occurred,Time Occurred,Area ID,Area Name,Reporting District,Crime Code,Crime Code Description,MO Codes,Victim Age,Victim Sex,Victim Descent,Premise Code,Premise Description,Weapon Used Code,Weapon Description,Status Code,Status Description,Crime Code 1,Crime Code 2,Crime Code 3,Crime Code 4,Address,Cross Street,Location

import pandas as pd
from flask import Flask, Response, render_template
app = Flask(__name__)
datasrc = './data/crime2010_2018.csv'

@app.route('/data')
def data():
    source = pd.read_csv(datasrc,skiprows=1,header=None,nrows=10000);
    src = source[[0,1,2,3,7,8,10,11,14,16,23,5,25]]
    src['lat'] = pd.DataFrame(src[25].str.replace('(','').str.replace(')','').str.split(', ').str[0])
    src['lng'] = pd.DataFrame(src[25].str.replace('(','').str.replace(')','').str.split(', ').str[1])
    data = src.rename(columns = {0 : 'num', 1 : 'date_reported',2:'date_occured',3:'time_occured',7:'crime_code',8:'crime_desc',10:'victim_age',11:'victim_sex',14:'premise_desc',16:'weapon',23:'address',5:'area',25:'location'})
    data[['lat','lng']] = data[['lat','lng']].apply(pd.to_numeric)
    data['date_occured'] = pd.to_datetime(source[2])
    data['date_reported'] = pd.to_datetime(source[1])
    data.drop('location', axis=1, inplace=True)
    response = data.to_json(orient='records')
    return Response(response, status=200, mimetype="application/json")

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.jinja_env.auto_reload = True
    app.config.update(
            DEBUG=True,
            TEMPLATES_AUTO_RELOAD=True
    )
    app.run()
