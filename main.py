from flask import Flask, render_template, redirect
import requests
import datetime
from pytz import timezone


app = Flask(__name__)

API_PATH = url = "https://api-basketball.p.rapidapi.com/games"
SEASON = "2020-2021"


@app.route("/")
def index():
    return render_template('index.html', datetime=datetime)


@app.route("/scores/<league>/<date>")
def scores(league, date):
    day = datetime.datetime.strptime(date, '%Y%m%d')
    date = day.strftime('%Y-%m-%d')

    params = {"date": date, "league": league}

    headers = {
        'x-rapidapi-key': "391968df82msh1003a5184eff750p11111cjsn539a19ed82a7",
        'x-rapidapi-host': "sportspage-feeds.p.rapidapi.com"
    }

    response = requests.get(url=API_PATH, headers=headers, params=params)
    games = response.json()['results']

    return render_template('scores-page.html', league=params['league'], games=games, today=day, datetime=datetime, timezone=timezone)


if __name__ == "__main__":
    app.run(debug=True)