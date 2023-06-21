import requests

# How to import from Forecast.py inside ForecastOptions folder

from MeteoWidget.ForecastOptions import ForecastAPI

class MeteoWidget():

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def create_request_string(self):
        #Get input as options and create request string according to it
        return ForecastAPI.FORECAST_BASE_URL+'latitude='+\
            str(self.latitude)+'&longitude='+str(self.longitude)+\
                '&hourly=temperature_2m'
    def get_forecast(self):
        
        res = requests.get(self.create_request_string())
        return res.json()
class MeteoWidgetConsole():
    def __init__(self):
        self.latitude = None
        self.longitude = None

    def get_input(self):
        self.latitude = float(input("Enter latitude: "))
        self.longitude = float(input("Enter longitude: "))

    def run(self):
        self.get_input()
        meteo_widget = MeteoWidget(self.latitude, self.longitude)
        forecast = meteo_widget.get_forecast()
        print(forecast)
