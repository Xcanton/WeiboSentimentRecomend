import sys
import re
import json
from bs4 import BeautifulSoup
from config.generalConfig import readFile
from parseConfig import featureProcess, interactUserFeatureList


def parseWBInteractUserFeature(filePath):
    html_doc = readFile(filePath)
    soup = BeautifulSoup(html_doc, "html.parser", from_encoding='utf-8')

    rawDicts = parseLogic(soup)

    featureDicts = []
    for rawDict in rawDicts:
        featureDict = featureProcess(rawDict, interactUserFeatureList)
        featureDicts.append(featureDict)
    return featureDicts


def parseLogic(soup):
    results = []
    user_regx = r"id=(?P<userId>\d+)"
    users = soup.find("div",{"class":"list_ul","node-type":"feed_list"}).contents
    for user in users:
        user_feature_dict = dict()

        try:
            user_raw = user.find("div",{"class":"WB_text"}).a['usercard']
            user_id_dict = re.search(user_regx,user_raw).groupdict()
            userId = user_id_dict['userId']

            userName = user.find("div",{"class":"WB_text"}).a.text
            text = user.find("div",{"class":"WB_text"}).span.text
            interactDate = user.find("div",{"class":"WB_from S_txt2"}).a['date']

            user_feature_dict['userId'] = userId
            user_feature_dict['userName'] = userName
            user_feature_dict['text'] = text
            user_feature_dict['interactDate'] = interactDate[:-4]  # ms->s

        except Exception as e:
            pass

        finally:
            if user_feature_dict != {} :
                results.append(user_feature_dict)

    return results




if __name__ == "__main__":
    # lines = sys.stdin.readlines()
    # for line in lines:
    line = "D:\JupyterWork\毕业设计\\6"
    jsonDicts = parseWBInteractUserFeature(line.strip())
    for jsonDict in jsonDicts:
        print(json.dumps(jsonDict))