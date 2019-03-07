#!/usr/bin/env python3
# coding=utf-8

import re

def testData():
    rawList = [
        "1037656074935984129,北海道胆振東部地震によりお亡くなりになられた方々にお悔やみを申し上げるとともに被災されたすべての方々に心よりお見舞いを申し上げます。自衛隊、警察、消防、海上保安庁が現時点で２万１千人、ヘリ５１機、艦船１２隻の態勢で救命・救助活動に… https://t.co/2mEk1Vu1AG,AbeShinzo,2018/09/06 19:57:41",
        "1037656095412576256,RT @AbeShinzo: 北海道胆振東部地震によりお亡くなりになられた方々にお悔やみを申し上げるとともに被災されたすべての方々に心よりお見舞いを申し上げます。自衛隊、警察、消防、海上保安庁が現時点で２万１千人、ヘリ５１機、艦船１２隻の態勢で救命・救助活動に取り組んでおり現在…,dragons_victory,2018/09/06 19:57:46",
        "1037656153176518656,RT @AbeShinzo: 北海道胆振東部地震によりお亡くなりになられた方々にお悔やみを申し上げるとともに被災されたすべての方々に心よりお見舞いを申し上げます。自衛隊、警察、消防、海上保安庁が現時点で２万１千人、ヘリ５１機、艦船１２隻の態勢で救命・救助活動に取り組んでおり現在…,MOPIRA,2018/09/06 19:58:00",
        "1037656159207940098,RT @AbeShinzo: 北海道胆振東部地震によりお亡くなりになられた方々にお悔やみを申し上げるとともに被災されたすべての方々に心よりお見舞いを申し上げます。自衛隊、警察、消防、海上保安庁が現時点で２万１千人、ヘリ５１機、艦船１２隻の態勢で救命・救助活動に取り組んでおり現在…,hayataka11,2018/09/06 19:58:01",
        "1037656211066241024,RT @AbeShinzo: 北海道胆振東部地震によりお亡くなりになられた方々にお悔やみを申し上げるとともに被災されたすべての方々に心よりお見舞いを申し上げます。自衛隊、警察、消防、海上保安庁が現時点で２万１千人、ヘリ５１機、艦船１２隻の態勢で救命・救助活動に取り組んでおり現在…,choki41,2018/09/06 19:58:14",
        "1037656214199390209,RT @AbeShinzo: 北海道胆振東部地震によりお亡くなりになられた方々にお悔やみを申し上げるとともに被災されたすべての方々に心よりお見舞いを申し上げます。自衛隊、警察、消防、海上保安庁が現時点で２万１千人、ヘリ５１機、艦船１２隻の態勢で救命・救助活動に取り組んでおり現在…,the_sintou,2018/09/06 19:58:14",
        "1037656236269789184,RT @AbeShinzo: 北海道胆振東部地震によりお亡くなりになられた方々にお悔やみを申し上げるとともに被災されたすべての方々に心よりお見舞いを申し上げます。自衛隊、警察、消防、海上保安庁が現時点で２万１千人、ヘリ５１機、艦船１２隻の態勢で救命・救助活動に取り組んでおり現在…,oochan2010,2018/09/06 19:58:20",
        "1037656277290082305,RT @AbeShinzo: 北海道胆振東部地震によりお亡くなりになられた方々にお悔やみを申し上げるとともに被災されたすべての方々に心よりお見舞いを申し上げます。自衛隊、警察、消防、海上保安庁が現時点で２万１千人、ヘリ５１機、艦船１２隻の態勢で救命・救助活動に取り組んでおり現在…,umbro47,2018/09/06 19:58:29",
        "1037656311054327809,RT @AbeShinzo: 北海道胆振東部地震によりお亡くなりになられた方々にお悔やみを申し上げるとともに被災されたすべての方々に心よりお見舞いを申し上げます。自衛隊、警察、消防、海上保安庁が現時点で２万１千人、ヘリ５１機、艦船１２隻の態勢で救命・救助活動に取り組んでおり現在…,everhiro,2018/09/06 19:58:37",
        "1037656342532509696,RT @AbeShinzo: 北海道胆振東部地震によりお亡くなりになられた方々にお悔やみを申し上げるとともに被災されたすべての方々に心よりお見舞いを申し上げます。自衛隊、警察、消防、海上保安庁が現時点で２万１千人、ヘリ５１機、艦船１２隻の態勢で救命・救助活動に取り組んでおり現在…,clarinet3710,2018/09/06 19:58:45",
            ]

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
            linksList.append({"source": sourceInfo["sourceUser"].lower(), "target": user_id.lower() })

        # if sourceUser["ifRaw"]:
        #     sourceInfo.update({"sourceUser": user_id})
        # else:
        #     linksList.append({"source": sourceUser["text"].lower(), "target": user_id.lower() })
        
        # textDict.update({sourceInfo["text"]: sourceInfo["sourceUser"]})

        

def getSourceText(text):
    sourceUser = re.findall(".*@(.*):.*", text)
    sourceText = re.findall(".*@.*:(.*)", text)
    if len(sourceUser) == 0:
        return {"ifRaw": True, "text": text}
    else:
        return {"ifRaw": False, "text": sourceText, "sourceUser": sourceUser}
