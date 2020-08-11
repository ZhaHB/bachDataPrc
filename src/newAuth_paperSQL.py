import re

from src.authorSQL import sourceTodict, author_depart_list


def getPID(articleID):
    articleIdBuff = []
    with open(file=articleID, encoding='utf-8')as urlList:
        for line in urlList.readlines():
            line = line.replace("\n", "")
            articleIdBuff.append(line)

    return articleIdBuff


def get_Aid_Pid_dict(authorbuff, paperbuff):
    APBuffdict = {}

    for key, val in authorbuff.items():
        for keys, values in val.items():
            APBuffdict[keys] = paperbuff[key]

    return APBuffdict


def generate_Aid_Pid_SQL(APbuff):
    with open("../sSQLgenerate/New_A_P_SQL.txt", 'w+', encoding='utf-8') as apfile:
        for key, val in APbuff.items():
            apfile.write("INSERT INTO `author_paper` VALUES (" + "\'" +str(val) + "\'"+", " + "\'" + str(key) + "\'" ");\n")


if __name__ == "__main__":
    fileSource = "../sdatasource/authors.txt"
    # articleUrl = "../datasource/url.txt"
    articleID = "../sdatasource/id.txt"

    authorSource = author_depart_list(fileSource)

    authorsDict = sourceTodict(authorSource)

    # print(authorsDict)

    artIDBuff = getPID(articleID)

    APbuff = get_Aid_Pid_dict(authorsDict, artIDBuff)

    generate_Aid_Pid_SQL(APbuff)

