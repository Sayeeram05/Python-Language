import requests


# print(WeatherData.status_code)  # == 200 working fine 

# print(WeatherData.json())

def CollectWeatherInfo(City):
    ApiKey = "e31bae8d59ead35b1fa5f3ad113d1d17"

    WeatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={City}&units=imperial&APPID={ApiKey}")

    Weather = WeatherData.json()["weather"][0]["main"]
    Temp = WeatherData.json()["main"]['temp']
    MinTemp  = WeatherData.json()["main"]['temp_min']
    MaxTemp =  WeatherData.json()["main"]['temp_max']
    Humidity = WeatherData.json()["main"]['humidity']

    Data = [Weather,Temp,MinTemp,MaxTemp,Humidity]

    return Data


if(__name__ == "__main__"):

    Weather,Temp,MinTemp,MaxTemp,Humidity = CollectWeatherInfo("chennai")

    print("Weather : ",Weather)
    print("Temp : ",Temp)
    print("Min Temp : ",MinTemp)
    print("Max Temp : ",MaxTemp)
    print("Humidity : ",Humidity)
