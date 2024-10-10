#!/usr/bin/env python
# coding: utf-8

import requests
import csv
import io

api_url = "https://data.moenv.gov.tw/api/v2"
dataset = "aqx_p_488"
format_type = "json"
offset = 0
limit = 1000

api_key = "your-api-key"

aqi_url = f"{api_url}/{dataset}?format={format_type}&offset={offset}&limit={limit}&api_key={api_key}"

response = requests.get(aqi_url)

aqi = None
if response.status_code == 200:
    try:
        data = response.json()
        print(type(data))
        if 'records' in data:
            aqi = data['records']
        else:
            print(f"找不到 records ，回應內容:\n {data}")
    except ValueError as e:
        print(f"JSON 無法正常解析: {e}")
        print(f"回應內容:\n{response.text}")
else:
    print(f"API 請求失敗，請檢查請求來源是否正確運作，狀態碼: {response.status_code}")
    print(f"回應內容:\n{response.text}")
    
for item in aqi :
    print(item["county"], item["sitename"], item["aqi"] ,item["pm2.5"])

with open("data_pm25.txt", "w", encoding="utf-8") as file:
    for item in aqi:
        file.write(f'{item["county"]}, {item["sitename"]}, AQI: {item["aqi"]}, PM2.5: {item["pm2.5"]}\n')