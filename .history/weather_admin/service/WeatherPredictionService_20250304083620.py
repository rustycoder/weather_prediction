import pickle
import numpy as np
from django.templatetags.static import static
import os

class WeatherPredictionService:

    def predict_weather_main(self, temperature, humidity, pressure):
        
        model_file_path = os.path.join(os.path.dirname(__file__), '../static/files/kathmandu_weather_data_model.pkl') 
        logger.debug(model_file_path)

        with open(model_file_path, 'rb') as m:
            kathmandu_weather_data_model = pickle.load(m)

        X = np.array([[temperature,humidity,pressure]])
        y = kathmandu_weather_data_model.predict(X)
        logger.debug(y[0])
        
        return y[0]