
# Python 爬取與存取API  擷取空氣品質 API
---

課堂作業：爬取空氣品質 PM2.5 的即時資訊 
抓取政府資料開放平台 `JSON` 資料 並做檔案處理


##  獲得資料方式

* `JSON` 格式：requests 獲取資料 python 直接解析

好用外掛工具 (chrome)：

> 查看 Web API json 格式：
> [https://chrome.google.com/webstore/detail/jsonview/](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc)

---
> 資料格式 : JSON、CSV、XML

>> Web API（Web Application Programming Interface）

>> [認識 Web API、HTTP 和 JSON 資料交換格式](https://tw.alphacamp.co/blog/api-introduction-understand-web-api-http-json)

關於 json 相關資料，之前做過的筆記：
[爬蟲下載圖片](https://medium.com/mr-wang/python-%E7%88%AC%E8%9F%B2%E6%8A%93%E5%8F%96%E5%9C%96%E7%89%87-ad1783fd401e)



## 資訊擷取來源


* [https://data.gov.tw/](https://data.gov.tw)

![](https://static.coderbridge.com/img/mrwang01/7f812f1495c2457dab774d63ba22ed78.png)

> 後來發現有更好用 最新試行版的 

> [環保署環境資料開放平台開放資料API](https://data.epa.gov.tw/api/v1)

>註冊 API Key 後可以篩選更多參數來撈資料



要解析的 json 網址：

* [http://opendata2.epa.gov.tw/AQI.json](http://opendata2.epa.gov.tw/AQI.json)
* [非公開 API ](https://data.epa.gov.tw/api/v1/aqx_p_432?offset=0&limit=80&api_key=自行註冊)


資料集名稱先記好比較快找到

![](https://data.epa.gov.tw/base/images/access_data_img_zh_02.png)

註冊 API 使用說明：
[https://data.epa.gov.tw/paradigm](https://data.epa.gov.tw/paradigm)





## request and json


透過 `json` 回傳的是一個 `list`


```python
import requests
aqi_url = "https://data.epa.gov.tw/api/v1/aqx_p_432?offset=0&limit=80&api_key=自行註冊" 
# 環保署環境資料開放平臺 試行版 https://data.epa.gov.tw/
# API 金鑰免費申請 ～
response = requests.get(aqi_url)
aqi = response.json()['records']
print(response.status_code)

### 200  正常回傳
### 404 回傳錯誤
print(type(response))
print(type(aqi))


```

![](https://static.coderbridge.com/img/mrwang01/8f8cccef2a934901ac68b62e16c60b7a.png)

## 輸出 List 

![](https://static.coderbridge.com/img/mrwang01/92475ef8e70f465492ae72420bb458e5.png)


## 檔案處理

“r” 唯讀模式

“w” 寫入模式（覆寫）

“a” 寫入模式（續寫）

`with open("data_pm25.txt", "w", encoding="utf-8") as file:`

再用 for 把資料寫入 file 當中



```python
f = open('file.txt', 'w')
f.write("file-write")
f.close()
```



## 參考資料
[輕鬆學習 Python | 資料分析](https://yaojenkuo.io/python-sklearn-cht/01-Web-Scraping-101-slides.pdf)


[輕鬆學習 Python：透過 API 擷取網站資料](https://medium.com/datainpoint/python-essentials-requesting-web-api-edd417a57ba5)


[Python 初學第十二講—檔案處理](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-bf0648108581)