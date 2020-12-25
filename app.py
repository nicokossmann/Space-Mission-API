from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
import datafunctions as data

df = data.load_data()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    results = data.get_all(df)
    return Response(results, mimetype='application/json')

@app.route('/organisation', methods=['GET'])
def data_of_name():
    name = request.args.get('name')
    results = data.get_by_name(df, name)
    return Response(results, mimetype='application/json')

@app.route('/datetime', methods=['GET'])
def data_of_date():
    date = request.args.get('date')
    year = request.args.get('year')
    from_year = request.args.get('from')
    to_year = request.args.get('to')
    if date is not None:
        results = data.get_by_date(df, date)
    elif year is not None:
        results = data.get_by_year(df, year)
    elif from_year is not None:
        results = data.get_by_from(df, from_year)
    elif to_year is not None:
        results = data.get_by_to(df, to_year)
    return Response(results, mimetype='application/json')

@app.route('/datetime/<from_year>/<to_year>')
def data_of_date_intervall(from_year=None, to_year=None):
    if from_year is not None and to_year is not None:
        results = data.get_by_from_to(df, from_year, to_year)
    return Response(results, mimetype='application/json')

