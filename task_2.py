import requests


def get_weather(city, api_key):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?&q={city}&appid={api_key}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data['name']
        current_temp = data['main']['temp']
        min_temp = data['main']['temp_min']
        max_temp = data['main']['temp_max']

        print(f"Weather in {city} now {current_temp}°C\n"
              f"The maximum temperature today is {max_temp}°C minimum {min_temp}°C")
    except Exception as ex:
        print(ex)


api_key = '0758913f0b040c9a1869964a0166a12a'


def main():
    city = input("Enter city: ")
    get_weather(city, api_key)


if __name__ == '__main__':
    main()