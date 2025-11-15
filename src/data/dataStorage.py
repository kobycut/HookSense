from .collectors import LocationCollector, WeatherCollector

class getWeatherFeatures:
    def __init__(self, location_name: str):
        self.location_collector = LocationCollector()
        self.weather_collector = WeatherCollector()
        lat, lon, city, state, country = self.location_collector.get_coordinates_from_name(location_name)
        self.weather_data = self.weather_collector.get_weather_data(city, state, country)

    def get_date_time(self):
        return self.weather_data['days'][0]['datetime']

    def get_temperature(self):
        # temperature in farhenheit
        return self.weather_data['days'][0]['temp']

    def get_humidity(self):
        return self.weather_data['days'][0]['humidity']

    def get_precipitation(self):
        return self.weather_data['days'][0]['precip']

    def get_precipitation_probability(self):
        return self.weather_data['days'][0].get('precipprob', None)

    def get_precipitation_type(self):
        return self.weather_data['days'][0].get('preciptype', None)

    def get_wind_speed(self):
        return self.weather_data['days'][0]['windspeed']

    def get_pressure(self):
        return self.weather_data['days'][0]['pressure']

    def get_cloud_cover(self):
        return self.weather_data['days'][0]['cloudcover']

    def get_visibility(self):
        return self.weather_data['days'][0]['visibility']

    def get_uv_index(self):
        return self.weather_data['days'][0]['uvindex']

    def get_sunrise(self):
        return self.weather_data['days'][0]['sunrise']

    def get_sunset(self):
        return self.weather_data['days'][0]['sunset']

    def get_moon_phase(self):
        return self.weather_data['days'][0]['moonphase']

