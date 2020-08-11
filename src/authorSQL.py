###############################
"""
DROP TABLE IF EXISTS `author`;
CREATE TABLE `author` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `authorName` varchar(255) NOT NULL,
  `atype` tinyint(4) DEFAULT NULL,
  `organization` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `publishNum` int(11) DEFAULT NULL,
  `citationNum` int(11) DEFAULT NULL,
  `Hindex` int(11) DEFAULT NULL,
  `Pindex` double(11,0) DEFAULT NULL,
  `researchInterests` varchar(255) DEFAULT NULL,
  `aminerIndex` int(11) DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=30513 DEFAULT CHARSET=utf8;
"""
###############################

import re


def author_depart_list(filesource):
    author_save_list = []
    with open(filesource, "r+", encoding='utf-8') as readfile:
        typeline = readfile.readlines()

        for author_per_art in typeline:
            if re.match(r'<.*?>', author_per_art):
                continue
            else:
                author_save_list.append(author_per_art)

    return author_save_list

"""
def author_list_dict(articleUrl, listSource):
    articleIdBuff = []
    authorIdDict = {}

    with open(file=articleUrl, encoding='utf-8')as urlList:
        for line in urlList:
            articleID = re.findall(r'\d+', line)
            for i in articleID:
                articleIdBuff.append(i)

    countANun = len(listSource)
    countnum = 0

    for i in range(0, countANun-1):
        for author in listSource[i]:
            countauthor = 0
            while countauthor < len(author):
                authorId = articleIdBuff[i]+ '.' + str(countauthor+1)
                countauthor += 1
                print(authorId)
    # print(articleIdBuff)
"""


def sourceTodict(listSource):
    wholeAuthorDict = {}
    countNum = 0
    courtWhoreDict = 0

    for item in listSource:
        perAuthorDict = {}

        item = item[:-1]   # 去除string结尾的\n
        authorList = item.split(",")

        for author in authorList:
            perAuthorDict[countNum+1] = author
            countNum += 1

        wholeAuthorDict[courtWhoreDict] = perAuthorDict

        courtWhoreDict += 1

    return wholeAuthorDict


def generateAuthorSQL(dictSource):
    with open("../sSQLgenerate/AuthorSQLgenerate.txt", 'w+', encoding='utf-8') as rfile:
        for dictItem in dictSource.values():
            for key, value in dictItem.items():
                value = value.lstrip()
                rfile.write("INSERT INTO `author` VALUES (" + '\'' +str(key) + "\'" + ", " + "\'" + str(value) + "\'" + ", " + " null, null, null, null, null, null, null, null, null);\n")


if __name__ == "__main__":
    fileSource = "../sdatasource/authors.txt"
    listSource = author_depart_list(fileSource)
    # author_list_dict(articleUrl, listSource)
    dictSource = sourceTodict(listSource)
    generateAuthorSQL(dictSource)
    # print(dictSource)





