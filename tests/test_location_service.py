#!/usr/bin/env python3
"""
Test script for LocationService to get coordinates from location names
"""

import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.data.collectors import LocationService, WeatherCollector

def test_location_service():
    """Test the LocationService with various locations"""

    print("Testing LocationService...")

    # Create an instance of LocationService
    location_service = LocationService()

    # Test locations
    test_location = "Norway"

    print(f"\n🗺️  Testing location: {test_location}")
    try:
        lat, lon = location_service.get_coordinates_from_name(test_location)
        print(f"✅ Coordinates for {test_location}: Lat {lat}, Lon {lon}")
    except Exception as e:
        print(f"❌ Error testing {test_location}: {e}")


def test_openweather_api():
    print("\nTesting OpenWeather...")
    location_service = LocationService()
    weather_service = WeatherCollector()

    test_location = "Provo"
    try:
        lat, lon = location_service.get_coordinates_from_name(test_location)
        print(weather_service.get_weather_data(lon, lat))
    except Exception as e:
        print(f"❌ Error testing {test_location}: {e}")

if __name__ == "__main__":
    print("🚀 Starting LocationService Tests")

    # Run the tests
    # test_location_service()
    test_openweather_api()

    print("\n✨ All tests completed!")