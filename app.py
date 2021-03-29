from flask import Flask, request, g
import sqlite3
import json
import PreProcessing
import SqlSide


app = Flask( __name__ )


if __name__ == "__main__":
    app.run(debug=True)


def connect_db():
    return sqlite3.connect('weather.db')


def handle_bad_request():
    return 'invalid input, longitude and latitude are not found', 400


@app.route('/weather/data')
def weather_forecast():
    longitude = request.args.get('lon')
    latitude = request.args.get('lat')
    g.db = connect_db()

    cur = g.db.execute(SqlSide.forecast_by_loc(), [longitude, latitude])
    records = cur.fetchall()

    if not records:
        return handle_bad_request()

    forecast_all_hours =[dict(forecast_time=row[0], precipitation_Rate_in_hr=row[1], temperature_Celsius=row[2])
                         for row in records]
    g.db.close()

    return json.dumps(forecast_all_hours, indent=4)


@app.route('/weather/summarize')
def weather_forecast_calculate():
    longitude = request.args.get('lon')
    latitude = request.args.get('lat')
    g.db = connect_db()

    cur = g.db.execute(SqlSide.summarize_forecast(), [longitude, latitude])
    row = cur.fetchone()
    if row[0] is None:
        return handle_bad_request()

    forecast_calculate = {'max': {'Temperature_Celsius': row[0], "Precipitation_Rate_in_hr": row[1]},
                          'min': {'Temperature_Celsius': row[2], "Precipitation_Rate_in_hr": row[3]},
                          'avg': {'Temperature_Celsius': row[4], "Precipitation_Rate_in_hr": row[5]}}
    g.db.close()

    return json.dumps(forecast_calculate, indent=4)
