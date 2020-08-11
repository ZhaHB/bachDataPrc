import re

from src.author_paperSQL import getPID


def getPtitle(titlePath):
    titleBuff = []
    with open(titlePath, 'r+', encoding='utf-8')as readfile:
        for line in readfile.readlines():
            line = line.replace("\n", "")
            if re.findall(r'<.*?>', line):
                continue
            else:
                titleBuff.append(line)
    return titleBuff


def getPAbs(absPath):
    absBuff = []
    with open(absPath, 'r', encoding='utf-8')as readfile:

        for line in readfile.readlines():

            line = line.replace("\n", "")

            if 0 < (len(line)) < 30:  # 未能找到较好的正则表达匹配法，此方法为规律性质的死办法
                continue

            elif len(line) == 0:
                absBuff.append('null')

            else:
                absBuff.append(line)

    return absBuff


def getPkeyword(keywordPath):
    keywordBuff = []

    with open(keywordPath, 'r+', encoding='utf-8')as readfile:
        for line in readfile.readlines():
            line = line.replace("\n", "")
            if re.findall(r'<.*?>', line):
                continue

            elif len(line) == 0:
                keywordBuff.append('null')

            else:
                keywordBuff.append(line)

    return keywordBuff


def getPUrl(urlPath):
    urlBuff = []
    with open(urlPath, 'r+', encoding='utf-8')as readfile:
        for line in readfile.readlines():
            line = line.replace("\n", "")
            if re.findall(r'<.*?>', line):
                continue
            else:
                urlBuff.append(line)
    return urlBuff


def generatePaperSQL(id, title, abs, keyword, url):
    countNum = len(id)
    with open("../SQLgenerate/paper.txt", 'r+', encoding='utf-8') as readfile:

        for i in range(countNum):
            readfile.write("INSERT INTO `paper` VALUES (" + "\'" + str(id[i]) + "\'" + ", " + "\'" + str(title[i]) + "\'" + ", " + "\'" + str(abs[i]) + "\'" + ", " + "\'" + str(keyword[i]) + "\'" + ", " + "'0' " + ", " + "\'" + str(url[i]) + "\'" + ", 'NCBI', '2020-02-08');\n")

    print("File writing OK...")

if __name__ == "__main__":
    # path for needed file
    articleUrl = "../datasource/url.txt"
    titlePath = "../datasource/title.txt"
    absPath = "../datasource/abstract.txt"
    keywordPath = "../datasource/keyword.txt"
    urlPath = "../datasource/url.txt"

    ########################################################

    paperID = getPID(articleUrl)
    paperTitle = getPtitle(titlePath)
    paperAbs = getPAbs(absPath)
    paperKeyword = getPkeyword(keywordPath)
    paperUrl = getPUrl(urlPath)

    ##############################test area###################
    generatePaperSQL(paperID, paperTitle, paperAbs, paperKeyword, paperUrl)
