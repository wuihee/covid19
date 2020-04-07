import requests
import json
import pandas as pd

url = 'https://api.covid19api.com/summary'
response = requests.get(url)
data = response.json()


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(data)

#df = pd.DataFrame(data)
