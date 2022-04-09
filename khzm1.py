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

        return "<h1>Hello 1 :"+str(datetime.now().second)+"</h1>"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
