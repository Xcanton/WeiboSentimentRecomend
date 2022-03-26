import os

from config.generalConfig import returnDirSubDir, returnDirSubFile
from parseRawWBHtml.interactUserFeature import parseWBInteractUserFeature
from parseRawWBHtml.mainTextFeature import parseWBMainText

base_Dir = "G:\\事件"
output_Dir = "G:\\data\\rawCsvData"
finished_file = "finished"
main_text_file = "mainTextFile"
user_text_file = "userTextFile"


if __name__ == "__main__":
    currentDir = ""
    currentFile = ""
    currentPageId = -1

    # 断点续传
    file = open(os.path.join(output_Dir, finished_file), "r", encoding="utf-8")
    doneList = [item.strip() for item in file.readlines()]
    file.close()

    for Dir in returnDirSubDir(base_Dir):

        currentDir = os.path.join(base_Dir, Dir)
        main_text_dict = parseWBMainText(os.path.join(currentDir, "1"))
        currentPageId = main_text_dict['servertime']

        if currentDir in doneList:
            pass
        else:
            with open(os.path.join(output_Dir, finished_file), "a", encoding="utf-8") as donefile:
                str_ = "\t".join([str(main_text_dict[item]) for item in main_text_dict.keys()])
                mainTextFile = open(os.path.join(output_Dir, main_text_file), "a", encoding="utf-8")
                mainTextFile.write("{0}\n".format(str_))
                mainTextFile.flush()
                mainTextFile.close()
                donefile.write("{0}\n".format(currentDir))
                donefile.flush()

        for filename in returnDirSubFile(currentDir):
            currentFile = os.path.join(currentDir, filename)
            if currentFile in doneList:
                continue
            userDictsList = parseWBInteractUserFeature(currentFile)

            for userDict in userDictsList:
                with open(os.path.join(output_Dir, finished_file), "a", encoding="utf-8") as donefile:
                    str_ = "\t".join([str(userDict[item]) for item in userDict.keys()])
                    userTextFile = open(os.path.join(output_Dir, user_text_file), "a", encoding="utf-8")
                    userTextFile.write("{0}\t{1}\n".format(currentPageId, str_))
                    userTextFile.flush()
                    userTextFile.close()
                    donefile.write("{0}\n".format(currentFile))
                    donefile.flush()

