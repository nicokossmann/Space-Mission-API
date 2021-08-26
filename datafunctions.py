import pandas as pd

def load_data():
    data = pd.read_csv('Space_Corrected.csv', sep=',')
    data = data.fillna(0)
    data['Organisation'] = data['Company Name']
    data['Mission'] = [details.split("|")[1].strip() for details in data['Detail']]
    data['Mission Status'] = data['Status Mission'] 
    data['Carrierrocket'] = [details.split("|")[0].strip() for details in data['Detail']]
    data['Rocket Status'] = data['Status Rocket']
    data['Costs'] = [str(cost).replace(",", "").strip() for cost in data[" Rocket"]]
    data['Datum']  = pd.to_datetime(data['Datum'])
    data['Date'] = [dt.date().strftime('%Y-%m-%d') for dt in data['Datum']]
    data['Time'] = [dt.time() for dt in data['Datum']]
    data['Launch Location'] = [list(map(str.strip, location.split(","))) for location in data['Location']]
    data = data.drop(columns=["Company Name", "Unnamed: 0", "Unnamed: 0.1", "Datum", " Rocket", "Detail", "Location", "Status Rocket", "Status Mission"])
    return data

def get_all(data):
    return data.to_json(orient="records", date_format='epoch',  date_unit='ms')

def get_by_missiondetails(data, string, value):
    results = data[data[string] == value]
    return results.to_json(orient="records", date_format='epoch', date_unit='ms')

def get_by_date(data, date):
    ts = pd.to_datetime(date)
    results = data[data['Date'] == ts.date()]
    return results.to_json(orient="records", date_format='epoch', date_unit='ms')

def get_by_year(data, year):
    ts = pd.to_datetime(year)
    results = data[pd.DatetimeIndex(data['Date']).year == ts.year]
    return results.to_json(orient="records", date_format='epoch', date_unit='ms')

def get_by_from(data, ge):
    ts = pd.to_datetime(ge)
    results = data[pd.DatetimeIndex(data['Date']).year >= ts.year]
    return results.to_json(orient="records", date_format='epoch', date_unit='ms')

def get_by_to(data, le):
    ts = pd.to_datetime(le)
    results = data[pd.DatetimeIndex(data['Date']).year <= ts.year]
    return results.to_json(orient="records", date_format='epoch', date_unit='ms')

def get_by_from_to(data, ge, le):
    ts_ge = pd.to_datetime(ge)
    ts_le = pd.to_datetime(le)
    results = data[pd.DatetimeIndex(data['Date']).year >= ts_ge.year]
    results = results[pd.DatetimeIndex(results['Date']).year <= ts_le.year]
    return results.to_json(orient="records", date_format='epoch', date_unit='ms')
    
def get_by_more(data, more):
    results = data[data['Costs'].astype(float) > float(more)]
    return results.to_json(orient="records", date_format='epoch', date_unit='ms')

def get_by_less(data, less):
    results = data[data['Costs'].astype(float) < float(less)]
    return results.to_json(orient="records", date_format='epoch', date_unit='ms')

def get_by_locationdetails(data, string, index):
    results = data[data['Launch Location'].apply(lambda x: x[index] == str(string))]
    return results.to_json(orient="records", date_format='epoch', date_unit='ms')

