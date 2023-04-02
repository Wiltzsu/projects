import requests, pycountry, datetime
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def index():

    # Default city
    default_city = 'Helsinki'
    default_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=5365bcb2d2de8c1a2a310b448e48f72a'
    x = requests.get(default_url.format(default_city)).json()

    helsinki_weather = {
        'city' : default_city,
        'country' : x['sys']['country'],
        'time' : x['timezone'],
        'temperature' : x['main']['temp'],
        'description' : x['weather'][0]['description'],
        'icon' : x['weather'][0]['icon'],
        'sunrise' : x['sys']['sunrise'],
        'sunset' : x['sys']['sunset']
    }

    # Get Finland's country code
    finland_code = helsinki_weather['country']
    # Convert country code to country name
    fi_name = pycountry.countries.get(alpha_2=finland_code).name

    # Convert json timezone to actual time
    helsinki_timezone = datetime.timezone(datetime.timedelta(seconds=helsinki_weather['time']))
    helsinki_time = datetime.datetime.now(tz=helsinki_timezone).strftime('%H:%M')

    # Get sunrise and sunset times
    helsinki_sunrise = helsinki_weather['sunrise']
    helsinki_sunset = helsinki_weather['sunset']

    # Set sunrise and sunset to readable time
    hki_sunrise = datetime.datetime.fromtimestamp(helsinki_sunrise, tz=helsinki_timezone).strftime('%H:%M')
    hki_sunset = datetime.datetime.fromtimestamp(helsinki_sunset, tz=helsinki_timezone).strftime('%H:%M')

    city_name = ''
    country_name = ''
    temperature = ''
    condition = ''
    desc = ''
    sunrise_time = ''
    sunset_time = ''
    local_time = ''

    # Request when searching
    if request.method == 'POST':
        city_name = request.form.get('city')
        x = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&units=metric&appid=5365bcb2d2de8c1a2a310b448e48f72a')
        json_object = x.json()

        # Get temperature, condition and description
        temperature = int(json_object['main']['temp'])
        condition = json_object['weather'][0]['main']
        desc = json_object['weather'][0]['description']

        # Get sunrise and sunset times and local timezone and time
        sunrise_timestamp = int(json_object['sys']['sunrise'])
        sunset_timestamp = int(json_object['sys']['sunset'])
        local_timezone = datetime.timezone(datetime.timedelta(seconds=json_object['timezone']))
        local_time = datetime.datetime.now(tz=local_timezone).strftime('%H:%M')

        # Set sunrise and sunset to readable format
        sunrise_time = datetime.datetime.fromtimestamp(sunrise_timestamp, tz=local_timezone).strftime('%H:%M')
        sunset_time = datetime.datetime.fromtimestamp(sunset_timestamp, tz=local_timezone).strftime('%H:%M')

        # Get country code
        country_code = json_object['sys']['country']
        # Convert country code to country name
        country_name = pycountry.countries.get(alpha_2=country_code).name

    # If no search, show Helsinki info as default
    else:
        city_name = default_city
        country_name = fi_name
        temperature = round(helsinki_weather['temperature'])
        condition = ''
        desc = helsinki_weather['description']
        sunrise_time = hki_sunrise
        sunset_time = hki_sunset
        local_time = helsinki_time

    # Weather in Scandinavian capitals
    cities = ['Helsinki', 'Stockholm', 'Oslo','Copenhagen', 'Reykjavik', 'Tórshavn']

    weather_info = []

    # Loop through the cities and get values
    for city in cities:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=5365bcb2d2de8c1a2a310b448e48f72a'.format(city)
        r = requests.get(url).json()

        #print(r)

        temp_celsius = round(r['main']['temp'])
        temp_feelslike = round(r['main']['feels_like'])
        wind_speed = round(r['wind']['speed'])
        
        # Convert wind direction from degrees to compass direction
        wind_direction = r['wind']['deg']
        wind_direction = round((wind_direction % 360) / 22.5)
        compass_direction = [
            "↓", "↙", "←", "↖", "↑", "↗", "→", "↘"
        ]
        wind_direction = compass_direction[int(wind_direction % 8)]
        
        weather = {
            'city': city,
            'temperature': temp_celsius,
            'temp_feels': temp_feelslike,
            'humidity': r['main']['humidity'],
            'wind': wind_speed,
            'wind_direction': wind_direction,
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_info.append(weather)

    return render_template('index.html', weather=weather_info, city_name=city_name, 
                           country_name=country_name, temperature=temperature, 
                           condition=condition, desc=desc, sunrise_time=sunrise_time, 
                           sunset_time=sunset_time, local_time=local_time,
                           helsinki_weather=helsinki_weather)
