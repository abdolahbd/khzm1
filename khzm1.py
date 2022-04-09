import time

import requests
from flask import Flask

app = Flask('')


@app.route('/')
def home():
    time.sleep(20)
    print(1)
    s = requests.Session()
    
    try:
        r = s.get('https://abdollah-prjt.herokuapp.com/',timeout=1)
    except:
        pass
    try:
        r = s.get('http://cfd8-105-71-19-104.ngrok.io',timeout=30)
    except:
        pass
    
    return "I'm alive"


def run():
    app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    app.run()
