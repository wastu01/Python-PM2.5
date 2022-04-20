#!/usr/bin/env python
# coding: utf-8

# In[19]:


import requests
aqi_url = "https://data.epa.gov.tw/api/v1/aqx_p_432?offset=0&limit=80&api_key=yourapi" 
# 環保署環境資料開放平臺 試行版 https://data.epa.gov.tw/
# API 金鑰免費申請 ～
response = requests.get(aqi_url)
aqi = response.json()['records']
# dict >> list
print(response.status_code)

### 200  正常回傳
### 404 回傳錯誤
print(type(response))
print(type(aqi))

for wa in aqi :
    print(wa["County"], wa["SiteName"], wa["PM2.5"])
    
    
with open("data_pm25.txt", "w", encoding="utf-8") as file:
     for list in aqi:
        file.write(f'{list["County"]} {list["SiteName"]} {list["PM2.5"]}\n')


# In[ ]:





# In[ ]:





# In[ ]:




