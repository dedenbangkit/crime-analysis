import pandas as pd
from flask import Flask, Response
app = Flask(__name__)
datasrc = './data/crime2010_2018.csv'

@app.route('/')
def index():
    source = pd.read_csv(datasrc,skiprows=1,header=None,nrows=1000)
    src = source[[1,2,3,7,8,10,11,16,25]]
    src['lat'] = pd.DataFrame(src[25].str.replace('(','').str.replace(')','').str.split(', ').str[0])
    src['lng'] = pd.DataFrame(src[25].str.replace('(','').str.replace(')','').str.split(', ').str[1])
    data = src.rename(columns = {1 : 'date_reported',2:'date_occured',3:'time_occured',7:'crime_code',8:'crime_description', 10:'victim_age',11:'victom_sex',16:'weapon',25:'location'})
    data[['lat','lng']] = data[['lat','lng']].apply(pd.to_numeric)
    data.drop('location', axis=1, inplace=True)
    response = data.to_json(orient='records')
    return Response(response, status=200, mimetype="application/json")

if __name__=='__main__':
    app.jinja_env.auto_reload = True
    app.config.update(
            DEBUG=True,
            TEMPLATES_AUTO_RELOAD=True
    )
    app.run()
