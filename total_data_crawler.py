                  ### 匯入套件
import requests
from bs4 import BeautifulSoup
import time
import os
import datetime
import csv

### 請求網頁並文字解析
######################## 需修改網址##################################################
while(True):
    url = input()
    # res = requests.get("http://uba.tw/107/Schedule/Details?scheduleId=2534D936-29EE-4521-97F9-E8A93BC0563F-")
    res = requests.get(url)
    # res.text

    ### 以 HTML 解析
    html = BeautifulSoup(res.text, "html.parser")

    ### 找尋 tag 為 tr 且 class 為 total_tr
    tr = html.find_all("tr", {"class" : "total_tr"})



    team_name_div = html.find_all('div', {"class" : 'record_tableTitle'})
    date = html.find('div',  {'class':"final_infoName"}).get_text()

    team_name1 = team_name_div[0].find('span').get_text()
    team_name2 = team_name_div[1].find('span').get_text()
    # print(team_name_div)
    date = date[:11] + date[15:20] 
    # print(date)
    date = time.strptime(date, "%Y年%m月%d日%H:%M")
    # print(date)
    ### 建立字典與參數
    column = ['日期', '隊伍', "二分", "二分%", "三分", "三分%", "罰球", "罰球%", "進攻", "防守", "總計", "助攻", "抄截", "阻攻", "失誤", "犯規", "得分", '勝負']
    total = {team_name1 : [],
            team_name2 : []}
    teams = [team_name1, team_name2]






    ### 比賽中有兩支隊伍需要爬取
    for i in range(2):
    
        team = [0 for k in range(len(column))] # 指定隊伍
        temp = tr[i]
        count = 0
        term = 2
        team[0] = time.strftime('%Y-%m-%d-%H-%M',date)
        team[1] = teams[i]
        for j in temp:
            
            if count >= 4 and j != "\n" and j.text != "":
                # print(j.text.strip(), column[term])
                team[term] = j.text.strip() # 將比賽資料依照順序放入字典
                term += 1
            else:
                count += 1
        # print(team)
        total[teams[i]] = team
    if int(total[team_name2][-2]) > int(total[team_name1][-2]):
        # print( total[team_name1][-2])
        total[team_name2][-1] = 1
        total[team_name1][-1] = 0
    else:
        total[team_name2][-1] = 0
        total[team_name1][-1] = 1
    # print(total[team_name2])
    data = [total[team_name1],total[team_name2]]
    '''Append new data after old output as csv, create a new output if old output not found'''
    header = column
    parsed_csv = data
    path = ''
    file_name = 'game_record'
    with open(os.path.join(path, file_name + "_output.csv"), mode='a+', newline='', encoding='UTF-8') as f:
        line = list(csv.reader(f))

    with open(os.path.join(path, file_name + "_output.csv"), mode='r', newline='',  encoding='UTF-8') as f:
        line = list(csv.reader(f))

    with open(os.path.join(path, file_name + "_output.csv"), mode='a+', newline='', encoding='UTF-8_sig') as csvfile:
        writer = csv.writer(csvfile)
        if len(line) == 0:
            print("第一次建立檔案")
            writer.writerow(header)
            writer.writerows(parsed_csv)
        else:
            for i in range(0, len(parsed_csv)):
                last_date = datetime.datetime.strptime(
                    line[len(line)-1][0], "%Y-%m-%d-%H-%M")
                current_date = datetime.datetime.strptime(
                    parsed_csv[i][0], "%Y-%m-%d-%H-%M")
                if current_date >= last_date:
                    print('新資料'+team_name1+team_name2)
                    writer.writerow(parsed_csv[i])