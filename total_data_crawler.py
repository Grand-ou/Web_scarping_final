### 匯入套件
import requests
from bs4 import BeautifulSoup

### 請求網頁並文字解析
res = requests.get("http://uba.tw/110/Schedule/Details?scheduleId=61E4C940-F182-4912-9241-7599A148EC52")
res.text

### 以 HTML 解析
html = BeautifulSoup(res.text, "html.parser")

### 找尋 tag 為 tr 且 class 為 total_tr
tr = html.find_all("tr", {"class" : "total_tr"})

### 建立字典與參數
total = {"NCCU" : {},
         "NTU" : {}}
teams = ["NCCU", "NTU"]
terms = ["二分", "%", "三分", "%", "罰球", "%", "進攻", "防守", "總計", "助攻", "抄截", "阻攻", "失誤", "犯規", "得分"]

### 比賽中有兩支隊伍需要爬取
for i in range(2):
    team = total[teams[i]] # 指定隊伍
    temp = tr[i]
    count = 0
    term = 0
    for j in temp:
        if count >= 4 and j != "\n" and j.text != "":
            team[terms[term]] = j.text.strip() # 將比賽資料依照順序放入字典
            term += 1
        else:
            count += 1
