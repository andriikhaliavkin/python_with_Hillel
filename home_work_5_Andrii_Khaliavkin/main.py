import requests

import pandas as pd


r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()['people']
pd_people = pd.DataFrame(people)
print(pd_people)
