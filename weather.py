from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods =['GET', 'POST'])
def base_page():
    city = request.form.get('city')
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=68ba69aec9e9c7d35e649ae55b0f7707"
    res = requests.get(url.format(city)).json()
    weather = {
        'city': city,
        'temperature': res['main']['temp'],
        'description': res['weather'][0]['description'],
        'icon': res['weather'][0]['icon'],
    }
    return render_template('weather.html', weather=weather)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
