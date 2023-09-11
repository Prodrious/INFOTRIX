#############################################
# Weather Checking Application
# Author : Rohith Prasad   (September 11, 2023)
# Purpose : To check for the weather of a specific place.
############################################

import requests
import argparse
import time

# Function to fetch weather data by city name
def weather(api_key, city):
    """
    Fetch weather data for a given city using the WeatherAPI.

    Parameters:
    - api_key (str): Your WeatherAPI API key.
    - city (str): The name of the city to check the weather for.

    Returns:
    - dict: Weather data in JSON format, or None if an error occurs.
    """
    base_url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("ERROR fetching weather data.")
        return None

# Function to add a city to the favorite list
def add_city(city, fav_city):
    """
    Add a city to the list of favorite cities.

    Parameters:
    - city (str): The city name to add.
    - fav_city (list): The list of favorite cities.

    Returns:
    - None
    """
    if city not in fav_city:
        fav_city.append(city)
        print(f"Successfully added {city} to the favorite list.")
    else:
        print(f"{city} is already in the list.")

# Function to remove a city from the favorite list
def remove_city(city, fav_city):
    """
    Remove a city from the list of favorite cities.

    Parameters:
    - city (str): The city name to remove.
    - fav_city (list): The list of favorite cities.

    Returns:
    - None
    """
    if city not in fav_city:
        print(f"{city} is not in the list.")
    else:
        fav_city.remove(city)
        print(f"{city} is removed successfully from the list.")

# Function to display the current list of favorite cities
def display_favorites(fav_city):
    """
    Display the list of favorite cities.

    Parameters:
    - fav_city (list): The list of favorite cities.

    Returns:
    - None
    """
    print("Favorite Cities:")
    for city in fav_city:
        print(city)

# Main function
def main():
    parser = argparse.ArgumentParser(description="Weather Checking Application")
    parser.add_argument("--city", help="Check weather by city name.")
    parser.add_argument("--add", help="Add a city to the favorite cities.")
    parser.add_argument("--remove", help="Remove a city from the favorite list.")
    parser.add_argument("--list", action="store_true", help="Display the favorite cities.")
    parser.add_argument("--api", help="Enter the API key for weatherapi.com.")
    args = parser.parse_args()

    # Default list of favorite cities
    fav_city = [
        'London', 'Los Angeles', 'Kochi', 'Jaipur', 'İstanbul', 
        'New York City', 'Philadelphia', 'Paris', 'San Diego', 'Agra', 'Tokyo'
    ]

    while True:
        if args.api:
            if args.city:
                data = weather(args.api, args.city)
                if data:
                    print(f"\nDate: {data['location']['localtime']}\nWeather in {args.city}\n{data['current']['temp_c']}°C Temperature  {data['current']['humidity']}g.m-3 Humidity\n{data['current']['condition']['text']}")
        if args.add:
            add_city(args.add, fav_city)
            break
        if args.remove:
            remove_city(args.remove, fav_city)
            break
        if args.list:
            display_favorites(fav_city)
        time.sleep(15)

if __name__ == "__main__":
    main()

################################################
# usage python weather.py --api <api_key> --city <city_name> (checking weather.)
# python weather.py --add/--remove <city_name> (adding or removing new city.)
# python weather.py --list (display the default list.)








