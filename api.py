import json
import requests

weather_api_url = 'http://api.weatherapi.com/v1'

api_key = '1d4cb7aa3af84e2ea53204140253001'

method = "/current.json"


# Requests information from the API using the get method
response = requests.get(weather_api_url + method, params={'key': api_key, 'q': 'Naples,Florida'})

print(response.json())

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Write the response data to response JSON file
    with open('response.json', 'w') as file:
        json.dump(response.json(), file, indent=4)
    print("The weather data has been written to 'response.json'.")
else:
    print(f"Failed to retrieve data: {response.status_code}")