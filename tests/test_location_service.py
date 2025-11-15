#!/usr/bin/env python3
"""
Test script for LocationService to get coordinates from location names
"""

import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.data.collectors import LocationCollector, WeatherCollector

def test_location_service():
    """Test the LocationService with various locations"""

    print("Testing LocationService...")

    # Create an instance of LocationCollector
    location_service = LocationCollector()

    # Test locations
    test_location = "oslo"

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
    test_location = "florence"

    try:
        lat, lon, city, state, country = location_collector.get_coordinates_from_name(test_location)
        print(f"Coordinates: Lat {lat}, Lon {lon}, City {city}, State {state}, Country {country}")
        moon_data = weather_collector.get_weather_data(city, state, country)
        print(f"✅ Moon data fetched successfully: {moon_data}")
    except Exception as e:
        print(f"❌ Error fetching moon cycle data: {e}")


if __name__ == "__main__":
    print("🚀 Starting LocationService Tests")

    # Run the tests
    test_location_service()
    test_weather_collector()

    print("\n✨ All tests completed!")