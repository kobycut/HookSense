from src.data.dataStorage import getWeatherFeatures
from datetime import datetime

class BaselineRuleModel:
    def __init__(self, location_name: str, date: str = None):
        """
        Initialize baseline model with location and optional date

        Args:
            location_name: Location string like "Miami, FL"
            date: Optional date string in 'YYYY-MM-DD' format. Defaults to today.
        """
        if date is None:
            date = datetime.today().strftime('%Y-%m-%d')

        self.getWeatherFeatures = getWeatherFeatures(location_name, date)

    def predict(self):
        score = 0
        score += self.score_temperature()
        score += self.score_precipitation()
        score += self.score_windspeed()
        score += self.score_pressure()
        score += self.score_cloud_cover()
        score += self.score_uv_index()
        score += self.score_moon_phase()
        return score

    def score_temperature(self):
        temp_total = 0.2  # weight assigned to temperature
        temp_f = self.getWeatherFeatures.get_temperature()

        if 65 <= temp_f <= 80:
            return temp_total  # ideal air temp range → full score
        elif 60 <= temp_f < 65 or 80 < temp_f <= 85:
            return temp_total * 0.75  # slightly outside ideal → partial score
        elif 55 <= temp_f < 60 or 85 < temp_f <= 90:
            return temp_total * 0.5  # marginal conditions
        elif 50 <= temp_f < 55 or 90 < temp_f <= 95:
            return temp_total * 0.25  # poor conditions
        else:
            return 0.0  # very cold or very hot → likely bad for fishing


    def score_precipitation(self):
        precip_total = 0.1
        precipitation = self.getWeatherFeatures.get_precipitation()

        if precipitation == 0:
            return precip_total * 0.7
        elif 0 < precipitation < 0.1:
            return precip_total
        elif 0.1 <= precipitation < 0.3:
            return precip_total * 0.7
        elif 0.3 <= precipitation:
            return precip_total * 0.3
        else:
            return 0.0

    def score_windspeed(self):
        wind_total = 0.15
        wind_speed = self.getWeatherFeatures.get_wind_speed()

        if wind_speed < 1:
            return wind_total * 0.3
        elif 1 <= wind_speed <= 4:
            return wind_total * 0.7
        elif 4 < wind_speed <= 12:
            return wind_total
        elif 12 < wind_speed <= 16:
            return wind_total * 0.6
        else:
            return 0.0

    def score_pressure(self):
        pressure_total = 0.2
        pressure_mb = self.getWeatherFeatures.get_pressure()
        pressure_hg = pressure_mb * 0.02953  # convert mb to inHg

        if 29.6 <= pressure_hg <= 30.4:
            return pressure_total  # stable/great
        elif 30.4 < pressure_hg <= 30.6 or 29.6 <= pressure_hg < 29.9:
            return pressure_total * 0.7  # ok-good
        elif 29.2 <= pressure_hg < 29.6:
            return pressure_total * 0.4  # falling → fish slow down
        else:
            return pressure_total * 0.2

    def score_cloud_cover(self):
        cloud_cover_total = 0.15
        cloud_cover = self.getWeatherFeatures.get_cloud_cover()

        if 70 <= cloud_cover <= 100:
            return cloud_cover_total  # overcast = great
        elif 40 <= cloud_cover < 70:
            return cloud_cover_total * 0.8  # partly cloudy
        elif 10 <= cloud_cover < 40:
            return cloud_cover_total * 0.6  # mostly sunny
        else:
            return cloud_cover_total * 0.3  # clear skies

    def score_uv_index(self):
        uv_total = 0.1
        uv_index = self.getWeatherFeatures.get_uv_index()

        if uv_index <= 2:
            return uv_total  # low UV = fish roam and feed more
        elif 3 <= uv_index <= 5:
            return uv_total * 0.7  # moderate UV
        elif 6 <= uv_index <= 7:
            return uv_total * 0.4  # high UV
        else:
            return uv_total * 0.2  # very high UV = fish hide deep

    def score_moon_phase(self):
        moon_total = 0.1
        moon_phase = self.getWeatherFeatures.get_moon_phase()

        if moon_phase <= 0.1 or moon_phase >= 0.9:
            return moon_total  # new or full moon
        elif 0.4 <= moon_phase <= 0.6:
            return moon_total * 0.6  # quarter → neutral
        else:
            return moon_total * 0.8  # waxing/waning → decent
