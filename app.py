from flask import Flask, request
import os
import requests

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

app = Flask(__name__)


def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, {"chat_id": chat_id, "text": text})


@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        chat_id = request.json["message"]["chat"]["id"]
        send_message(chat_id, "hello")
    return {"ok": True}


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=80)
