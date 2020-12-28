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

@app.route('/missions', methods=['GET'])
def data_of_mission():
    organisation = request.args.get('organisation')
    mission = request.args.get('mission')
    mission_status = request.args.get('missionsatus')
    rocket = request.args.get('rocket')
    rocket_status = request.args.get('rocketstatus')
    if organisation is not None:
        results = data.get_by_missiondetails(df, 'Organisation', organisation)
    elif mission is not None:
        results = data.get_by_missiondetails(df, 'Mission', mission) 
    elif mission_status is not None:
        results = data.get_by_missiondetails(df, 'Mission Status', mission_status)
    elif rocket is not None:
        results = data.get_by_missiondetails(df, 'Carrierrocket', rocket)
    elif rocket_status is not None:
        results = data.get_by_missiondetails(df, 'Rocket Status', rocket_status)
    return Response(results, mimetype='application/json')


@app.route('/missions/costs', methods=['GET'])
def data_of_budget():
    more = request.args.get('more')
    less = request.args.get('less')
    if more is not None:
        results = data.get_by_more(df, more)
    elif less is not None:
        results = data.get_by_less(df, less)
    return Response(results, mimetype='application/json')

@app.route('/date', methods=['GET'])
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

@app.route('/date/<from_year>/<to_year>', methods=['GET'])
def data_of_date_intervall(from_year=None, to_year=None):
    if from_year is not None and to_year is not None:
        results = data.get_by_from_to(df, from_year, to_year)
    return Response(results, mimetype='application/json')

@app.route('/location', methods=['GET'])
def data_of_location():
    spacecenter = request.args.get('spacecenter')
    country = request.args.get('country')
    if spacecenter is not None:
        results = data.get_by_locationdetails(df, spacecenter, 1)
    elif country is not None:
        results = data.get_by_locationdetails(df, country, -1)
    return Response(results, mimetype='application/json')
