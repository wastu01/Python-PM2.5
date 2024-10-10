# Python-PM2.5
 
 抓取政府資料開放平台提供的 空氣品質指標（AQI）的數據，再篩選出 PM2.5 的數據

 2024 更新：平臺 API 網址有更換過，參數換成小寫形式，請參考 [環境部環境資料開放平臺](https://data.moenv.gov.tw/paradigm) 說明。

 2024-10-10 問題紀錄：獲取資料時遇到無法從平台得到完整資料的問題，並回傳下列訊息：

 ```
can't parse JSON. Raw result:

<br />
<b>Notice</b>: fwrite(): Write of 642092 bytes failed with errno=28 No space left on device in <b>/var/www/html/Ap/app/Module/Office/JsonModuleImpl.php</b> on line <b>31</b><br />

 ```

目前想法：把 limit 降低或是用迴圈一次只獲取特定天數的資料，但偶爾還是會回傳錯誤。

## 執行畫面

> [Python-PM2.5-DataAnalyzing](https://wastu01.github.io/article/python-pm25-aqi-opendata/)