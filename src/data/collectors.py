from ..utils.config import Config
import requests


class LocationService:
    def get_coordinates_from_name(self, location_name: str):
        API_key = Config.OPENWEATHER_API_KEY
        api_call = f'http://api.openweathermap.org/geo/1.0/direct?q={location_name}&limit=5&appid={API_key}'
        try:
            response = requests.get(api_call)
            response.raise_for_status()
            data = response.json()
            if data:
                print(f'Coordinates for {location_name}: Lat {data[0]["lat"]}, Lon {data[0]["lon"]}')
                return data[0]['lat'], data[0]['lon']
        except Exception as e:
            print(f'Error fetching coordinates for {location_name}: {e}')
            raise

class WeatherCollector:
    def get_weather_data(self, longitude: float, latitude: float):
        API_key = Config.OPENWEATHER_API_KEY
        api_call = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_key}'
        response = requests.get(api_call)
        response.raise_for_status()
        return response.json()

class TemperatureCollector:
    pass

class RainfallCollector:
    pass

class BarometricPressureCollector:
    pass

class WindSpeedCollector:
    pass

class CloudCoverCollector:
    pass

class MoonCycleCollector:
    pass
