import requests
import time
import pandas as pd


def get_weather_and_time(city: str, api_key: str):
    """
    Fetches real-time weather and time information for a given city.

    Args:
        city: The name of the city.
        api_key: The API key for the weather service.

    Returns:
        A dictionary containing weather information and potentially time, or None
        if the API call fails.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric" # Using metric units for temperature

    try:
        response = requests.get(complete_url)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        # Extract weather information
        weather_info = {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "city": data["name"],
            "country": data["sys"]["country"],
            "sunrise": data["sys"]["sunrise"],
            "sunset": data["sys"]["sunset"],
            "timezone": data["timezone"]
        }

        # Although OpenWeatherMap doesn't provide current time directly,
        # we can calculate it using the timezone offset and sunrise/sunset times
        # For simplicity and to meet the 'time information' requirement,
        # we'll include sunrise and sunset as they are time-related data from the API.

        return weather_info

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        if response.status_code == 401:
            print("Error: Invalid API key. Please check your key.")
        elif response.status_code == 404:
            print(f"Error: City '{city}' not found.")
        else:
            print(f"Error: Received status code {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    except KeyError as e:
        print(f"Error parsing weather data: Missing key {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def get_current_time_list():
  current_time = time.strftime("%H:%M:%S", time.localtime())
  list_results = []
  list_results.append(current_time) # Corrected to append the current time
  return list_results # Corrected to return the list


time_clock_list = get_current_time_list() # Renamed variable for clarity
run = True
while run: # Simplified while loop condition
      api_key = 'f922c280eb1a14d3a41e2b4de7910726' # Consider storing API key more securely
      city = input("Enter the name of the city: ")

      if city.lower() == 'quit': # Corrected quit condition
        run = False
      else:
        weather_info = get_weather_and_time(city, api_key)
        results_Wheater = []

        if weather_info: # Check if weather_info was successfully retrieved
            Model = [
                ("Temperatura : " + str(weather_info["temperature"]) + " °C"),
                ("Cidade : " + str(weather_info["city"])),
                ("Descrição : " + str(weather_info["description"])),
                ("Umidade : " + str(weather_info["humidity"]) + "%"),
                ("Velocidade do vento : " + str(weather_info["wind_speed"]) + " m/s")

            ]

            current_time_str = time_clock_list[0] # Get the time string from the list

            for modelo in Model:
                print(modelo)
                result = f"{modelo} - {current_time_str}" # Concatenate string with time string
                results_Wheater.append(result) # Append the result to the list



            def generation_data(list_city : list )
                while run ==True:
                      for city in list_city:
                        print(weather_info = get_weather_and_time(city, api_key))
                        for result in results_Wheater:
                            Interface_model = (f"{city}  \nData {}")











