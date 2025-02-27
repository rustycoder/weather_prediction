from abc import ABC, abstractmethod

class OpenWeatherService(ABC):
  
    @abstractmethod
    def current_weather_data(self, latitude, longitude):
        # https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
        pass
    
    @abstractmethod
    def five_day_weather_forecast(self, latitude, longitude):
        # api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
        pass

    @abstractmethod
    def weather_maps(self, layer, zoom, x, y):
        # https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={API key}
        # Layers : clouds_new, precipitation_new, pressure_new, wind_new, temp_new, 
        pass

    @abstractmethod
    def current_air_pollution_data(self, latitude, longitude):
        # http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API key}
        pass

    @abstractmethod
    def forecast_air_pollution_data(self, latitude, longitude):
        # http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={API key}
        pass

    @abstractmethod
    def historical_air_pollution_data(self, latitude, longitude, start, end):
        # http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={API key}
        # http://api.openweathermap.org/data/2.5/air_pollution/history?lat=508&lon=50&start=1606223802&end=1606482999&appid={API key}
        pass

    @abstractmethod
    def geocoding(self, query, limit):
        # http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
        # http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={API key}
        pass

