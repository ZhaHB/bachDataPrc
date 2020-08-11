import re


def getId(idpath):
    idBuff = []
    with open(idpath, 'r+', encoding='utf-8')as readfile:
        for line in readfile.readlines():
            line = line.replace("\n", "")
            idBuff.append(line)
    return idBuff


def getAbs(abspath):
    absBuff = []
    with open(abspath, 'r+', encoding='utf-8')as readfile:
        for line in readfile.readlines():
            line = line.replace("\n", "")
            if re.findall("is null", line):
                absBuff.append("null")
                print("N_a")
            else:
                absBuff.append(line)
    return absBuff


def getTitle(titlepath):
    titleBuff = []
    with open(titlepath, 'r+', encoding='utf-8')as readfile:
        for line in readfile.readlines():
            line = line.replace("\n", "")
            titleBuff.append(line)
    return titleBuff


def getKeyword(keywordpath):
    keywordBuff = []
    with open(keywordpath, 'r+', encoding='utf-8')as readfile:
        for line in readfile.readlines():
            line = line.replace("\n", "")
            if re.findall("is null", line) or len(line) == 0:
                keywordBuff.append("null")

                print("N_K")

            else:
                keywordBuff.append(line)
    return keywordBuff


def generatePaperSQL(idBuffer, titleBuffer, absBuffer, keywordBuffer):
    countNum = len(idBuffer)
    with open("../sSQLgenerate/paper/" + keyword + "_newpaper.txt", 'w+', encoding='utf-8') as readfile:
        for i in range(countNum):
            readfile.write("INSERT INTO `paper` VALUES (" + "\'" + str(idBuffer[i]) + "\'" + ", " + "\'" + str(
                titleBuffer[i]) + "\'" + ", " + "\'" + str(absBuffer[i]) + "\'" + ", " + "\'" + str(
                keywordBuffer[i]) + "\'" + ", " + "'0' " + ", " + "\'" + "https://www.ncbi.nlm.nih.gov/pubmed/" + str(idBuffer[i]) + "\'" + ", 'NCBI', '2020-02-08');\n")

    print("File writing OK...")


if __name__ == "__main__":
    keywordbuffer = ["bacteriology", "botany", "cell", "disease", "fungus", "gene", "genetics", "kinase",
                     "neurobiology", "protein", "virology", "zoology"]

    for keyword in keywordbuffer:

        idPath = "../SdataN_46/" + keyword + "_ge_pid.txt"
        absPath = "../SdataN_46/" + keyword + "_abs.txt"
        titlePath = "../SdataN_46/" + keyword + "_title.txt"
        keywordPath = "../SdataN_46/" + keyword + "_keyword.txt"

        idBuffer = getId(idPath)
        absBuffer = getAbs(absPath)
        titleBuffer = getTitle(titlePath)
        keywordBuffer = getKeyword(keywordPath)

        print(len(idBuffer))
        print(len(absBuffer))
        print(len(titleBuffer))
        print(len(keywordBuffer))

        generatePaperSQL(idBuffer, titleBuffer, absBuffer, keywordBuffer)
