import sys
import re
import json
from bs4 import BeautifulSoup
from config.generalConfig import readFile
from parseConfig import mainTextFeatureDict, featureProcess


def parseWBMainText(filePath):
    html_doc = readFile(filePath)
    soup = BeautifulSoup(html_doc, "html.parser", from_encoding='utf-8')
    rawDict = parseLogic(soup)
    featureDict = featureProcess(rawDict, mainTextFeatureDict)
    return featureDict


def parseLogic(soup):
    scriptList = soup.find_all('script')[3].text.replace("\nvar $CONFIG = {};\n", "").split("; \n")

    result = dict()
    retext = r".*'(?P<config_key>\w+)']='(?P<value>\w+)'"

    # 推文配置
    for script in scriptList:
        try:
            reDict = re.search(retext, script).groupdict()
            if reDict is not None:
                result[reDict['config_key']] = reDict['value']
        except Exception as e :
            pass

    # 推文正文
    try:
        mainText = soup.find_all("div")[2].div.contents[23].div.contents[3].div.div.div.div.div.div.contents[5].contents[7]
        if mainText is not None:
            result['mainText'] = mainText.text.strip()
    except Exception as e:
        pass

    # 推文评分
    try:
        likeCnt = soup.find("em", {"class":"W_ficon ficon_praised S_txt2"}).parent.contents[1].text
        result['likeCnt'] = likeCnt
    except Exception as e:
        pass
    try:
        commentCnt = soup.find("em", {"class":"W_ficon ficon_repeat S_ficon"}).parent.contents[1].text
        result['commentCnt'] = commentCnt
    except Exception as e:
        pass
    try:
        zhuanfaCnt = soup.find("em", {"class":"W_ficon ficon_forward S_ficon"}).parent.contents[1].text
        result['zhuanfaCnt'] = zhuanfaCnt
    except Exception as e:
        pass

    return result




if __name__ == "__main__":
    # lines = sys.stdin.readlines()
    # for line in lines:
    #     jsonDict = parseWBMainText(line.strip())
    #     print(json.dumps(jsonDict))
    line = "D:\JupyterWork\毕业设计\\6"
    jsonDict = parseWBMainText(line.strip())
    print(json.dumps(jsonDict))
