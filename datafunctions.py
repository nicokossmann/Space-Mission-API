import pandas as pd

def load_data():
    data = pd.read_csv('Space_Corrected.csv', sep=',')
    data['Datum']  = pd.to_datetime(data['Datum'])
    data['Date'] = [dt.date() for dt in data['Datum']]
    data['Time'] = [dt.time() for dt in data['Datum']]
    data['Cost'] = data[" Rocket"]
    data = data.drop(columns=["Unnamed: 0", "Unnamed: 0.1", "Datum", " Rocket"])
    return data

def get_by_name(data, name):
    results = data[data['Company Name'] == name]
    return results.to_json(orient="records", date_format='iso')

def get_by_date(data, date):
    ts = pd.to_datetime(date)
    results = data[data['Date'] == ts.date()]
    return results.to_json(orient="records", date_format='iso')

def get_by_year(data, year):
    ts = pd.to_datetime(year)
    results = data[pd.DatetimeIndex(data['Date']).year == ts.year]
    return results.to_json(orient="records", date_format='iso')
