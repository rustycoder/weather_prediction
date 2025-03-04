from weather_prediction.settings import OPEN_API_KEY, OPEN_API_DATA_URL, OPEN_API_GEO_URL, OPEN_API_MAP_URL

from datetime import datetime
import requests
import pandas as pd


class OpenWeatherService:

    def current_weather_data(self, latitude, longitude):
        # https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
        url = OPEN_API_DATA_URL + f"weather?lat={latitude}&lon={longitude}&appid={OPEN_API_KEY}"
        try:
            response = requests.get(url)
            response.raise_for_status()  

            weather_data = response.json()
            weather_data['dt'] = datetime.fromtimestamp(weather_data['dt'])

            return weather_data, None
        except requests.exceptions.RequestException as e:
            return None, str(e)
        except Exception as e: 
            return None, str(e)
    
    def current_weather_search(self, location):
        # https://api.openweathermap.org/data/2.5/weather?q=Tokyo&appid=ad7a0d3241b9002f727b41ce4323a46d
        url = OPEN_API_DATA_URL + f"weather?q={location}&appid={OPEN_API_KEY}"
        try:
            response = requests.get(url)
            response.raise_for_status()  

            weather_data = response.json()
            weather_data['dt'] = datetime.fromtimestamp(weather_data['dt'])

            return weather_data, None
        except requests.exceptions.RequestException as e:
            return None, str(e)
        except Exception as e: 
            return None, str(e)
        
    

    def five_day_weather_forecast(self, latitude, longitude):
        # https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}
        url = OPEN_API_DATA_URL + f"forecast?lat={latitude}&lon={longitude}&appid={OPEN_API_KEY}"
        try:
            response = requests.get(url)
            response.raise_for_status()  

            weather_forecast = response.json()

            return weather_forecast, None
        except requests.exceptions.RequestException as e:
            return None, str(e)
        except Exception as e: 
            return None, str(e)

    def weather_maps(self, layer, zoom, x, y):
        # https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={API_key}
        # Layers : clouds_new, precipitation_new, pressure_new, wind_new, temp_new
        url = OPEN_API_MAP_URL + f"{layer}/{zoom}/{x}/{y}.png?appid={OPEN_API_KEY}"
        try:
            response = requests.get(url)
            response.raise_for_status()  

            weather_maps = response.json()

            return weather_maps, None
        except requests.exceptions.RequestException as e:
            return None, str(e)
        except Exception as e: 
            return None, str(e)

    def current_air_pollution_data(self, latitude, longitude):
        # http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_key}
        url = OPEN_API_DATA_URL + f"air_pollution?lat={latitude}&lon={longitude}&appid={OPEN_API_KEY}"
        try:
            response = requests.get(url)
            response.raise_for_status()  

            air_pollution_data = response.json()
            air_pollution_data['list'][0]['dt'] = datetime.fromtimestamp(air_pollution_data['list'][0]['dt'])
            qualitative_name = {1:'Good', 2:'Fair', 3:'Moderate', 4:'Poor', 5:'Very Poor'}
            air_pollution_data['list'][0]['main']['qualitative_name'] = qualitative_name.get(air_pollution_data['list'][0]['main']['aqi'])

            return air_pollution_data, None
        except requests.exceptions.RequestException as e:
            return None, str(e)
        except Exception as e: 
            return None, str(e)

    def forecast_air_pollution_data(self, latitude, longitude):
        # http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={API_key}
        url = OPEN_API_DATA_URL + f"air_pollution/forecast?lat={latitude}&lon={longitude}&appid={OPEN_API_KEY}"
        try:
            response = requests.get(url)
            response.raise_for_status()  

            air_pollution_forecast = response.json()
            qualitative_name = {1:'Good', 2:'Fair', 3:'Moderate', 4:'Poor', 5:'Very Poor'}
            for l in air_pollution_forecast['list']:
                l['dt_txt'] = datetime.fromtimestamp(l['dt'])
                l['main']['qualitative_name'] = qualitative_name.get(l['main']['aqi'])


            return air_pollution_forecast, None
        except requests.exceptions.RequestException as e:
            return None, str(e)
        except Exception as e: 
            return None, str(e)

    def historical_air_pollution_data(self, latitude, longitude, start, end):
        # http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={API_key}
        # http://api.openweathermap.org/data/2.5/air_pollution/history?lat=508&lon=50&start=1606223802&end=1606482999&appid={API_key}
        url = OPEN_API_DATA_URL + f"air_pollution/history?lat={latitude}&lon={longitude}&start={start}&end={end}&appid={OPEN_API_KEY}"
        try:
            response = requests.get(url)
            response.raise_for_status()  

            air_pollution_history = response.json()

            return air_pollution_history, None
        except requests.exceptions.RequestException as e:
            return None, str(e)
        except Exception as e: 
            return None, str(e)

    def geocoding(self, query, limit):
        # http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API_key}
        # http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={API_key}
        url = OPEN_API_GEO_URL + f"?q={query}&limit={limit}&appid={OPEN_API_KEY}"
        try:
            response = requests.get(url)
            response.raise_for_status()  

            geocoding = response.json()

            return geocoding, None
        except requests.exceptions.RequestException as e:
            return None, str(e)
        except Exception as e: 
            return None, str(e)