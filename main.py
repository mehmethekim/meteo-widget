import requests
from MeteoWidget import MeteoWidget

meteo_widget = MeteoWidget(52.91, 21.00)
print(meteo_widget.get_forecast())