import time

import requests
from flask import Flask

app = Flask('')


@app.route('/')
def home():
    time.sleep(2)
    print(1)
    s = requests.Session()
    r = s.get('https://abdollah-prjt.herokuapp.com/',timeout=1)
    r = s.get('http://cfd8-105-71-19-104.ngrok.io',timeout=1)
    return "I'm alive"


def run():
    app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    app.run()
