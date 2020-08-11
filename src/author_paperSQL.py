import re

from src.authorSQL import sourceTodict, author_depart_list


def getPID(articleUrl):
    articleIdBuff = []
    with open(file=articleUrl, encoding='utf-8')as urlList:
        for line in urlList:
            articleID = re.findall(r'\d+', line)
            for i in articleID:
                articleIdBuff.append(i)

    return articleIdBuff


def get_Aid_Pid_dict(authorbuff, paperbuff):
    APBuffdict = {}

    for key, val in authorbuff.items():
        for keys, values in val.items():
            APBuffdict[keys] = paperbuff[key]

    return APBuffdict


def generate_Aid_Pid_SQL(APbuff):
    with open("../SQLgenerate/A_P_SQL.txt", 'w+', encoding='utf-8') as apfile:
        for key, val in APbuff.items():
            apfile.write("INSERT INTO `author_paper` VALUES (" + "\'" +str(val) + "\'"+", " + "\'" + str(key) + "\'" ");\n")


if __name__ == "__main__":
    fileSource = "../datasource/authors.txt"
    articleUrl = "../datasource/url.txt"

    authorSource = author_depart_list(fileSource)

    authorsDict = sourceTodict(authorSource)

    # print(authorsDict)

    artIDBuff = getPID(articleUrl)

    APbuff = get_Aid_Pid_dict(authorsDict, artIDBuff)

    generate_Aid_Pid_SQL(APbuff)

