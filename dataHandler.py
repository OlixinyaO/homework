#!/usr/bin/env python3
# coding=utf-8

import re
import csv
import json

def testData():
    rawList = [
        "1037830994621911041,RT @taikokoji: こんばんは(こんばんは) 今週9日日曜日に開催予定でした、ラブライブ！サンシャイン!!Aqours クラブ活動 LIVE &amp; FAN MEETING 2018 ユニット対抗全国ツアー 札幌公演が、6日の朝発生した北海道胆振東部地震に伴い、本日未…,Koumt,2018/09/07 07:32:45",
        "1037831108723765249,RT @PrefHokkaido: ≪　平成30年北海道胆振東部地震に関する情報　≫停電解消戸数の状況は本日9月7日3時現在で、96万4千戸となっています。電力に関する最新情報はこちらからご覧ください。https://t.co/ahe8bGOifd,ah_love_yuki,2018/09/07 07:33:12"]
    # csv_reader = csv.reader(open("./rawData/Hokkaido.csv", 'r', encoding='UTF-8'))
    # i = 0
    # for row in csv_reader:
    #     if i != 0:
    #         rawList.append(row)
    #     i = i + 1

    return rawList

def transRawToDict():
    rawList = testData()
    textDict = {}
    userList = []
    nodesList = []
    linksList = []
    for x in rawList:
        xList = x.split(',')
        id = xList[0]
        text = xList[1]
        user_id = xList[2]
        create_time = xList[3]
        sourceInfo = getSourceText(text)

        if user_id not in userList:
            userList.append(user_id)
            nodesList.append({"name": user_id, "category": 0, "id": user_id.lower()})
        # 1. 人名做节点
        if sourceInfo["ifRaw"] is False:
            linkInfo = json.dumps({"source": sourceInfo["sourceUser"].lower(), "target": user_id.lower() })
            linksList.append(linkInfo)

    fp = open("./showData/test.json", 'w', encoding='UTF-8')
    fp.write(linksList)
    fp.close()

        

def getSourceText(text):
    sourceUser = re.findall(".*@(.*)", text.split(':')[0])
    if len(sourceUser) == 0:
        return {"ifRaw": True}
    else:
        return {"ifRaw": False, "sourceUser": sourceUser[0]}

transRawToDict()

t1 = "RT @taikokoji: こんばんは(こんばんは) 今週9日日曜日に"
t2 = "RT @PrefHokkaido: ≪　平成30年北海道胆振東部地震に関"

# getSourceText(t1)
# getSourceText(t2)
