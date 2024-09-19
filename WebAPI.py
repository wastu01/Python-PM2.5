#!/usr/bin/env python
# coding: utf-8
import requests
aqi_url = "https://data.moenv.gov.tw/api/v2/aqx_p_432?offset=0&limit=1000&api_key=your-api-key" 

response = requests.get(aqi_url)
aqi = response.json()['records']

print(response.status_code)
print(type(response))
print(type(aqi))

for wa in aqi :
    print(wa["County"], wa["SiteName"], wa["PM2.5"])
    
with open("data_pm25.txt", "w", encoding="utf-8") as file:
     for list in aqi:
        file.write(f'{list["County"]} {list["SiteName"]} {list["PM2.5"]}\n')