import time
from datetime import datetime

import web
from urllib.request import urlopen
import requests

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        time.sleep(2)
        print(1)
        print('--------------')
        # Making a get request
        # create a session object
        s = requests.Session()



        # again make a get request
        r = s.get('https://abdollah-prjt.herokuapp.com/',timeout=1)
        r = s.get('http://127.0.0.1:1234/',timeout=1)

        # check if cookie is still set
        #response = requests.get('http://127.0.0.1:8080/')
        return "<h1>Hello 1 :"+str(datetime.now().second)+"</h1>"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
