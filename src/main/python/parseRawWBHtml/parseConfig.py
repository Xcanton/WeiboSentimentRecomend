mainTextFeatureDict = {
    "servertime": "Int",
    "uid": "Int",
    "title_value": "String",
    "onick": "String",
    "nick": "String",

    "likeCnt": "Int",
    "commentCnt": "Int",
    "zhuanfaCnt": "Int",

    "mainText": "String"
}

interactUserFeatureList = {
    'userId': "Int",
    'userName': "String",
    'interactDate': "Int",
    'text': "String"
}


def typeFormatOrDefault(oriValue: None, type_: str, isReal: bool):
    if type_ == "Int" and not isinstance(oriValue, int):
        return [-1, int(oriValue)][isReal]
    elif type_ == "String" and not isinstance(oriValue, str):
        return ["", str(oriValue)][isReal]
    else:
        return oriValue


def featureProcess(rawDict: dict, FeatureDict) -> dict:

    featureDict = dict()

    for featureName in FeatureDict.keys():
        isReal = featureName in rawDict.keys()

        try:
            if isReal:
                featureValue = typeFormatOrDefault(rawDict[featureName], FeatureDict[featureName], isReal)
                featureDict[featureName] = featureValue
            else:
                featureValue = typeFormatOrDefault(None, FeatureDict[featureName], isReal)
                featureDict[featureName] = featureValue
        except Exception as e:
            featureValue = typeFormatOrDefault(None, FeatureDict[featureName], False)
            featureDict[featureName] = featureValue

    return featureDict