from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
import datafunctions as data


app = Flask(__name__)
df = data.load_data()

@app.route('/', methods=['GET'])
def index():
    return '<h1>Welcome to Space-Mission-API<h1>'

@app.route('/organisation', methods=['GET'])
def data_of_name():
    name = request.args.get('name')
    results = data.get_by_name(df, name)
    return Response(results, mimetype='application/json')

@app.route('/datetime', methods=['GET'])
def data_of_date():
    date = request.args.get('date')
    year = request.args.get('year')
    if date is not None:
        results = data.get_by_date(df, date)
    elif year is not None:
        results = data.get_by_year(df, year)
    return Response(results, mimetype='application/json')
