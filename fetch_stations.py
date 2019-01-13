#SUTD MIT hackathon
#weather fetcher

import json
from pprint import pprint
import requests

apiKey = '1223637cea762bdfca012ff07ef8eeea'

r= requests.get('http://api.openweathermap.org/data/2.5/weather?q=Singapore&APPID={1223637cea762bdfca012ff07ef8eeea}')
print(r.json())
