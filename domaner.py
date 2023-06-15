import requests
from datetime import date,timedelta
url = "https://data.internetstiftelsen.se/bardate_domains.json"
r = requests.get(url, verify=False)

#print(r.json())

json = r.json()


date = date.today()
tomorrow = date.today() + timedelta(days=1)
print(date)
print(tomorrow)


for data in json["data"]:
    #print(data)
    if data["release_at"] == str(tomorrow):
        print(data)
#print(json["data"][0])