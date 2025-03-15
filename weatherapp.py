import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def main():
    api_key = "your_api_key_here"
    city = input("Enter the city name: ")
    weather_data = get_weather(api_key, city)
    
    if weather_data.get('cod') != 200:
        print("City not found!")
        return
    
    print(f"Weather in {city}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Weather: {weather_data['weather'][0]['description']}")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")

if __name__ == "__main__":
    main()