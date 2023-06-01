import requests
import json

def weather_update(city):
    API_KEY = '7c98cb283ffa581112f47e983f53c5a0'  # Replace with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for unsuccessful requests
        data = response.json()

        # Extract relevant information from the response
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        # Display the weather forecast
        print(f"Weather forecast for {city}:")
        print(f"Conditions: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    except requests.exceptions.HTTPError as error:
        print(f"HTTP error occurred: {error}")
    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")
    except KeyError:
        print(f"Failed to parse weather data.")
    except json.JSONDecodeError:
        print(f"Failed to decode JSON response.")

if __name__ == '__main__':
    city_name = input("Enter the city name: ")
    weather_update(city_name)
