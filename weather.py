# from flask import Flask, request, render_template
# import json
# import urllib.request
# import requests # for making http req to unsplash

# app = Flask(__name__)

# DEFAULT_IMAGES = {   # Example
#     "default": "/static/img.jpeg"  # Your default image
# }

# #api keys
# api = "f8118dc35570e33751823677c06db752"  # API key
# UNSPLASH_API_KEY = "jr4ABD2KCra3sFzho3AihWBxeLSNnn6Om7j9ijXZMeM"

# @app.route('/', methods=['POST', 'GET'])
# def weather():
#     city = request.form.get('city','chennai')
#     image_url = DEFAULT_IMAGES['default']

    

#     url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
#     source = urllib.request.urlopen(url).read()

#     list_of_data = json.loads(source)

#     data = {
#         "country_code": str(list_of_data['sys']['country']),
#         "coordinate": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
#         "temp": f"{list_of_data['main']['temp']} K",
#         "pressure": str(list_of_data['main']['pressure']),
#         "humidity": str(list_of_data['main']['humidity']),
#     }

   


#     try:
#         headers = {"Authorization": f"Client-ID {UNSPLASH_API_KEY}"}
#         unsplash_url = f"https://api.unsplash.com/search/photos?query={city}" # Unsplash API endpoint
#         image_response = requests.get(unsplash_url, headers=headers)
#         image_response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
#         image_data = image_response.json()

#         if image_data['results']: # Check if there any results
#             image_url = image_data['results'][0]['urls']['regular'] # Get the 'regular' size image URL
#         else:
#             image_url = DEFAULT_IMAGES['default'] # Fallback to predefined if no results from Unsplash

#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching image from Unsplash: {e}")
#         image_url = DEFAULT_IMAGES['default'] # Fallback to predefined

#     print(data)
#     return render_template('index1.html', data=data , image_url=image_url)


from flask import Flask, request, render_template
import json
import urllib.request
import requests

app = Flask(__name__)

# API Keys (Set in environment variables - IMPORTANT!)
OPENWEATHER_API_KEY = "f8118dc35570e33751823677c06db752" 
UNSPLASH_API_KEY = "jr4ABD2KCra3sFzho3AihWBxeLSNnn6Om7j9ijXZMeM"

DEFAULT_IMAGES = {
    "default": "/static/img.jpg",  # Correct path! img.jpg, not img.jpeg
    "clear": "/static/sunny.jpg",
    "clouds": "/static/cloudy.jpg",
    "rain": "/static/rain.jpg",
    "thunderstorm": "/static/thunderstorm.jpg",
    "drizzle": "/static/rain.jpg",
    "snow": "/static/snow.jpg",
    "mist": "/static/mist.jpg",
    "smoke": "/static/mist.jpg",
    "haze": "/static/mist.jpg",
    "fog": "/static/mist.jpg",
}

@app.route('/', methods=['POST', 'GET'])
def weather():
    city = request.form.get('city', 'chennai')
    image_url = DEFAULT_IMAGES['default']
    weather_data = None

    try:
        # 1. Fetch weather data (as before, with error handling)
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}'
        source = urllib.request.urlopen(url).read()
        list_of_data = json.loads(source)

        weather_data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
            "temp": f"{list_of_data['main']['temp']} K",
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "description": str(list_of_data['weather'][0]['main']).lower()
        }

        # 2. Fetch image from Unsplash (CORRECTED URL and fallback logic)
        try:
            headers = {"Authorization": f"Client-ID {UNSPLASH_API_KEY}"}
            unsplash_url = f"https://api.unsplash.com/search/photos?query={city}"  # Correct URL!
            image_response = requests.get(unsplash_url, headers=headers)
            image_response.raise_for_status()
            image_data = image_response.json()

            if image_data['results']:
                image_url = image_data['results'][0]['urls']['small']
            else:
                image_url = DEFAULT_IMAGES.get(weather_data['description'], DEFAULT_IMAGES['default']) # Correct fallback

        except requests.exceptions.RequestException as e:
            print(f"Error fetching image from Unsplash: {e}")
            image_url = DEFAULT_IMAGES.get(weather_data['description'], DEFAULT_IMAGES['default']) # Correct fallback

    except Exception as e:
        print(f"Error fetching weather data: {e}")
        weather_data = {"error": "Error fetching weather data. Please check the city name and API key."}

    return render_template('index1.html', data=weather_data, image_url=image_url)


if __name__ == '__main__':
    app.run(debug=True)