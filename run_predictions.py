from datetime import datetime
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.models.Baseline import BaselineRuleModel
from src.models.RandomTree import RandomTreeModel
from src.data.dataStorage import getWeatherFeatures

def run_baseline_predictions():
    location = "sydney"
    date = datetime.today().strftime('%Y-%m-%d')
    weather_features = getWeatherFeatures(location, date)
    baseline_model = BaselineRuleModel(location, date)

    print("Date and Time:", weather_features.get_date_time())
    print("Location:", location)
    print("Features: ", '\n',
        {"Temperature": weather_features.get_temperature()}, '\n',
        {"Humidity": weather_features.get_humidity()}, '\n',
        {"Precipitation": weather_features.get_precipitation()}, '\n',
        {"Wind Speed": weather_features.get_wind_speed()}, '\n',
        {"Pressure": weather_features.get_pressure()},'\n',
        {"Cloud Cover": weather_features.get_cloud_cover()},'\n',
        {"Visibility": weather_features.get_visibility()},'\n',
        {"UV Index": weather_features.get_uv_index()},'\n',
        {"Sunrise": weather_features.get_sunrise()},'\n',
        {"Sunset": weather_features.get_sunset()},'\n',
        {"Moon Phase": weather_features.get_moon_phase()},'\n',
    )
    print("Baseline Prediction:", baseline_model.predict() * 100)


def run_random_tree_predictions():
    location = "sydney"
    date = datetime.today().strftime('%Y-%m-%d')
    weather_features = getWeatherFeatures(location, date)
    random_tree_model = RandomTreeModel(location)

    random_tree_model.generate_historical_labels(num_samples=100)
    random_tree_model.prepare_training_data()
    random_tree_model.save_training_data()
    random_tree_model.train_model()

    prediction = random_tree_model.predict()
    print("Random Tree Prediction:", prediction * 100)


if __name__ == "__main__":
    run_baseline_predictions()
    run_random_tree_predictions()