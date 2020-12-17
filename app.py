from flask import Flask, app, render_template
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine('mysql+pymysql://zsks:zsks@198.144.179.169:3306/zsks')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<tablename>")
def sqltoweb(tablename):
    df = pd.read_sql(tablename,engine)
    hdata = df.to_html
    return render_template('index.html',tables=[hdata(classes='data', header="true")])


if __name__ == '__main__':
    app.run(debug = True)