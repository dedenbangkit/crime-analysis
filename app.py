from flask import Flask, Response, render_template
from app.api import db, field
app = Flask(__name__)

@app.route('/')
def index():
    codes = [7,8]
    group = ['crime_code', 'crime_desc']
    return render_template('index.html', categories=field(codes, group))

@app.route('/api/data')
def data():
    response = db()
    return Response(response, status=200, mimetype="application/json")

if __name__=='__main__':
    app.jinja_env.auto_reload = True
    app.config.update(
            DEBUG=True,
            TEMPLATES_AUTO_RELOAD=True
    )
    app.run()
