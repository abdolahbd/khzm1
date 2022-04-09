import time

import web
from urllib.request import urlopen
import requests
import os

os.environ["PORT"] = "1245"

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
        
        try:
            r = s.get('https://abdollah-prjt.herokuapp.com/',timeout=1)
        except:
            pass
        try:
            r = s.get('http://127.0.0.1:1234/',timeout=1)
        except:
            pass
      

        # check if cookie is still set
        #response = requests.get('http://127.0.0.1:8080/')
        return "<h1>Hello 1 </h1>"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
