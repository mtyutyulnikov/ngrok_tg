from flask import Flask, request
import os
import requests

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

app = Flask(__name__)


def send_message(chat_id, text):
    weather_url = "https://api.open-meteo.com/v1/forecast?latitude=55.0415&longitude=82.9346&current=temperature_2m&hourly=temperature_2m&timezone=Asia%2FBangkok&forecast_days=1"
    weather_data = requests.get(weather_url).json()
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    text = f"Температура сейчас : {weather_data['current']['temperature_2m']} \nТемпература через 24 ч : {weather_data['hourly']['temperature_2m'][-1]}"
    requests.post(url, {"chat_id": chat_id, "text": text})


@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        chat_id = request.json["message"]["chat"]["id"]
        send_message(chat_id, "hello")
    return {"ok": True}


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=80)
