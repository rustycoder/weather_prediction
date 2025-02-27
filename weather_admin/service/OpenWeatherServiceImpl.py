from weather_admin.service.interface import OpenWeatherService
from weather_prediction.settings import OPEN_API_KEY, OPEN_API_DATA_URL, OPEN_API_GEO_URL, OPEN_API_MAP_URL

from loguru import logger
from datetime import datetime
import requests


class OpenWeatherServiceImpl:

    def current_weather_data(self, latitude, longitude):
        # https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
        url = OPEN_API_DATA_URL + f"weather?lat={latitude}&lon={longitude}&appid={OPEN_API_KEY}"
        logger.debug(url)
        try:
            logger.info("Getting Current Weather Data...")
            response = requests.get(url)
            response.raise_for_status()  

            weather_data = response.json()
            logger.debug(weather_data['dt'])
            weather_data['dt'] = datetime.fromtimestamp(weather_data['dt'])

            return weather_data, None
        except requests.exceptions.RequestException as e:
            return None, str(e)
        except Exception as e: 
            return None, str(e)
    
    def five_day_weather_forecast(self, latitude, longitude):
        # https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}
        url = OPEN_API_DATA_URL + f"forecast?lat={latitude}&lon={longitude}&appid={OPEN_API_KEY}"
        logger.debug(url)
        try:
            logger.info("Getting Five Day Weather Forecast...")
            response = requests.get(url)
            response.raise_for_status()  

            weather_data = response.json()

            return weather_data, None
        except requests.exceptions.RequestException as e:
            return None, str(e)
        except Exception as e: 
            return None, str(e)

    def weather_maps(self, layer, zoom, x, y):
        # https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={API_key}
        # Layers : clouds_new, precipitation_new, pressure_new, wind_new, temp_new
        url = OPEN_API_MAP_URL + f"{layer}/{zoom}/{x}/{y}.png?appid={OPEN_API_KEY}"
        logger.debug(url)
        try:
            logger.info("Getting Weather Maps...")
            response = requests.get(url)
            response.raise_for_status()  

            weather_data = response.json()

            return weather_data, None
        except requests.exceptions.RequestException as e:
            return None, str(e)
        except Exception as e: 
            return None, str(e)

    def current_air_pollution_data(self, latitude, longitude):
        # http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_key}
        url = OPEN_API_DATA_URL + f"air_pollution?lat={latitude}&lon={longitude}&appid={OPEN_API_KEY}"
        logger.debug(url)
        try:
            logger.info("Getting Air Pollution Data...")
            response = requests.get(url)
            response.raise_for_status()  

            weather_data = response.json()

            return weather_data, None
        except requests.exceptions.RequestException as e:
            return None, str(e)
        except Exception as e: 
            return None, str(e)

    def forecast_air_pollution_data(self, latitude, longitude):
        # http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={API_key}
        url = OPEN_API_DATA_URL + f"air_pollution/forecast?lat={latitude}&lon={longitude}&appid={OPEN_API_KEY}"
        logger.debug(url)
        try:
            logger.info("Getting Forecast Air Pollution Data...")
            response = requests.get(url)
            response.raise_for_status()  

            weather_data = response.json()

            return weather_data, None
        except requests.exceptions.RequestException as e:
            return None, str(e)
        except Exception as e: 
            return None, str(e)

    def historical_air_pollution_data(self, latitude, longitude, start, end):
        # http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={API_key}
        # http://api.openweathermap.org/data/2.5/air_pollution/history?lat=508&lon=50&start=1606223802&end=1606482999&appid={API_key}
        url = OPEN_API_DATA_URL + f"air_pollution/history?lat={latitude}&lon={longitude}&start={start}&end={end}&appid={OPEN_API_KEY}"
        logger.debug(url)
        try:
            logger.info("Getting Forecast Air Pollution Data...")
            response = requests.get(url)
            response.raise_for_status()  

            weather_data = response.json()

            return weather_data, None
        except requests.exceptions.RequestException as e:
            return None, str(e)
        except Exception as e: 
            return None, str(e)

    def geocoding(self, query, limit):
        # http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API_key}
        # http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={API_key}
        url = OPEN_API_GEO_URL + f"?q={query}&limit={limit}&appid={OPEN_API_KEY}"
        logger.debug(url)
        try:
            logger.info("Getting Geocoding...")
            response = requests.get(url)
            response.raise_for_status()  

            weather_data = response.json()

            return weather_data, None
        except requests.exceptions.RequestException as e:
            return None, str(e)
        except Exception as e: 
            return None, str(e)