from ..utils.config import Config
import requests
from datetime import datetime


class LocationCollector:
    def get_coordinates_from_name(self, location_name: str):
        API_key = Config.OPENWEATHER_API_KEY
        api_call = f'http://api.openweathermap.org/geo/1.0/direct?q={location_name}&limit=5&appid={API_key}'
        try:
            response = requests.get(api_call)
            response.raise_for_status()
            data = response.json()
            if data:
                location = data[0]
                lat = location['lat']
                lon = location['lon']
                city = location.get('name', '')
                state = location.get('state', '')
                country = location.get('country', '')

                if state and len(state) > 2:
                    state = self._convert_state_abbrev(state)

                return lat, lon, city, state, country
        except Exception as e:
            print(f'Error fetching coordinates for {location_name}: {e}')
            raise

    def _convert_state_abbrev(self, state_name: str) -> str:
        us_state_abbrev = {
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 	'TX',
            'Utah':	'UT',
            'Vermont':	'VT',
            'Virginia':	'VA',
            'Washington':	'WA',
            'West Virginia':	'WV',
            'Wisconsin':	'WI',
            'Wyoming':	'WY'
            }
        return us_state_abbrev.get(state_name.lower(), state_name)

class WeatherCollector:
    def get_weather_data(self, city: str, state: str = '', country: str = '', date: str = ''):
        try:
            API_KEY = Config.VISUAL_CROSSING_API_KEY
            if state:
                location_str = f"{city},{state}"
            elif country:
                location_str = f"{city},{country}"
            else:
                location_str = city
            elements_relevant_to_fishing = 'datetime,temp,humidity,precip,preciptype,precipprob,windspeed,cloudcover,visibility,moonphase,sunrise,sunset,uvindex,pressure,'
            api_call = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location_str}/{date}?unitGroup=us&key={API_KEY}&include=days&elements={elements_relevant_to_fishing}'
            response = requests.get(api_call)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f'Error fetching moon cycle data: {e}')
            raise
