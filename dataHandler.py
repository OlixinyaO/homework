#!/usr/bin/env python3
# coding=utf-8

import re
import csv
import json

def testData():
    rawList = [
        # "1037830994621911041,RT @taikokoji: こんばんは(こんばんは) 今週9日日曜日に開催予定でした、ラブライブ！サンシャイン!!Aqours クラブ活動 LIVE &amp; FAN MEETING 2018 ユニット対抗全国ツアー 札幌公演が、6日の朝発生した北海道胆振東部地震に伴い、本日未…,Koumt,2018/09/07 07:32:45",
        # "1037831108723765249,RT @PrefHokkaido: ≪　平成30年北海道胆振東部地震に関する情報　≫停電解消戸数の状況は本日9月7日3時現在で、96万4千戸となっています。電力に関する最新情報はこちらからご覧ください。https://t.co/ahe8bGOifd,ah_love_yuki,2018/09/07 07:33:12"
        ]
    csv_reader = csv.reader(open("./rawData/Hokkaido.csv", 'r', encoding='UTF-8'))
    i = 0
    for row in csv_reader:
        if i != 0:
            rawList.append(row)
        i = i + 1

    return rawList

def transRawToDict():
    rawList = testData()
    textDict = {}
    userList = []
    nodesList = []
    linksList = []
    timedict = {}
    timeList = []
    for x in rawList:
        xList = x
        # xList = x.split(",")
        id = xList[0]
        text = xList[1]
        user_id = xList[2]
        create_time = xList[3]
        sourceInfo = getSourceText(text)

        minute_time = create_time[:-3]

        if minute_time not in timedict:
            timedict[minute_time] = 1
            timeList.append(minute_time)
        else:
            timedict[minute_time] += 1

        if user_id not in userList:
            userList.append(user_id)
            nodeinfo = {"name": user_id, "category": 0, "id": user_id.lower() }
            nodesList.append(nodeinfo)

        if sourceInfo["ifRaw"] is False:
            linkInfo = {"source": sourceInfo["sourceUser"].lower(), "target": user_id.lower() }
            linksList.append(linkInfo)

    
    timeList.sort()
    yCountList = []
    for time in timeList:
        yCountList.append(timedict[time])
    
    saveLineDataInfile(timeList, yCountList)
    saveNewDataInfile(linksList, nodesList)

def saveNewDataInfile(linksList, nodesList):
    fp = open("./showData/netData.json", 'w', encoding='UTF-8')
    fp.write("loadNetData(")
    fp.write(json.dumps({
        "type": "force",
        "categories": ["rawUser"],
        "links": linksList,
        "nodes": nodesList}))
    fp.write(")")
    fp.close()

def saveLineDataInfile(timeList, yCountList):
    fp = open("./showData/lineChartData.json", 'w', encoding='UTF-8')
    fp.write("loadLineChartData(")
    fp.write(json.dumps({
        "timeList": timeList,
        "yCountList": yCountList}))
    fp.write(")")
    fp.close()      

def getSourceText(text):
    sourceUser = re.findall(".*@(.*)", text.split(':')[0])
    if len(sourceUser) == 0:
        return {"ifRaw": True}
    else:
        return {"ifRaw": False, "sourceUser": sourceUser[0]}

transRawToDict()

# getSourceText(t1)
# getSourceText(t2)
