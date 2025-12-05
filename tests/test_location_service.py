#!/usr/bin/env python3
"""
Test script for LocationService to get coordinates from location names
"""

import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.data.collectors import LocationCollector, WeatherCollector
from src.data.dataStorage import getWeatherFeatures
from src.models.Baseline import BaselineRuleModel
from src.models.RandomTree import RandomTreeModel

location_name = 'provo'


def test_location_service():
    """Test the LocationService with various locations"""

    print("Testing LocationService...")

    # Create an instance of LocationCollector
    location_service = LocationCollector()

    # Test locations
    test_location = location_name

    print(f"\n🗺️  Testing location: {test_location}")
    try:
        lat, lon, city, state, country = location_service.get_coordinates_from_name(test_location)
        print(f"✅ Coordinates for {test_location}: Lat {lat}, Lon {lon}")
    except Exception as e:
        print(f"❌ Error testing {test_location}: {e}")

def test_weather_collector():
    print("\nTesting WeatherCollector...")
    weather_collector = WeatherCollector()
    location_collector = LocationCollector()
    test_location = location_name

    try:
        lat, lon, city, state, country = location_collector.get_coordinates_from_name(test_location)
        print(f"Coordinates: Lat {lat}, Lon {lon}, City {city}, State {state}, Country {country}")
        moon_data = weather_collector.get_weather_data(city, state, country)
        print(f"✅ Moon data fetched successfully: {moon_data}")
    except Exception as e:
        print(f"❌ Error fetching moon cycle data: {e}")

def test_dataStorage():
    print("\nTesting DataStorage...")

    try:
        data_cleaner = getWeatherFeatures(location_name)

        date_time = data_cleaner.get_date_time()
        temperature = data_cleaner.get_temperature()
        humidity = data_cleaner.get_humidity()
        precipitation = data_cleaner.get_precipitation()
        precipitation_probability = data_cleaner.get_precipitation_probability()
        precipitation_type = data_cleaner.get_precipitation_type()
        wind_speed = data_cleaner.get_wind_speed()
        pressure = data_cleaner.get_pressure()
        cloud_cover = data_cleaner.get_cloud_cover()
        visibility = data_cleaner.get_visibility()
        uv_index = data_cleaner.get_uv_index()
        sunrise = data_cleaner.get_sunrise()
        sunset = data_cleaner.get_sunset()
        moon_phase = data_cleaner.get_moon_phase()

        print(f"✅ DataStorage fetched successfully: {date_time}, {temperature}F, {humidity}%, {precipitation}in, {precipitation_probability}%, {precipitation_type}, {wind_speed}mph, {pressure}mb, {cloud_cover}%, {visibility}mi, UV Index {uv_index}, Sunrise {sunrise}, Sunset {sunset}, Moon Phase {moon_phase}")
    except Exception as e:
        print(f"❌ Error testing DataStorage: {e}")

def test_predict_with_baseline_model():
    print("\nTesting BaselineRuleModel...")
    try:
        model = BaselineRuleModel(location_name)
        score = model.predict()
        print(f"✅ BaselineRuleModel prediction score for {location_name}: {score * 100}")
    except Exception as e:
        print(f"❌ Error testing BaselineRuleModel: {e}")


def test_predict_random_tree_model():
    print("\Testing RandomTreeModel...")

    try:
        model = RandomTreeModel(location_name)
        score = model.predict()
        print(f"✅ BaselineRuleModel prediction score for {location_name}: {score}")
    except Exception as e:
        print(f"❌ Error testing RandomTreeModel: {e}")

if __name__ == "__main__":
    print("🚀 Starting LocationService Tests")

    # Run the tests
    test_location_service()
    test_weather_collector()
    test_dataStorage()
    test_predict_with_baseline_model()
    test_predict_random_tree_model()

    print("\n✨ All tests completed!")