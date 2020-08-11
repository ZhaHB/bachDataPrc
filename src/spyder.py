# This is a file for finding data source from PubMed

#################################
#   Import Area
#
#################################
import requests
import re
# import time
# import os


#################################
# define URL
url = "https://www.ncbi.nlm.nih.gov/pubmed/?term="
sourceUrl = "https://www.ncbi.nlm.nih.gov/pubmed/"
#################################


################################
# define savepath
path = 'C:/Users/asus/Desktop/Datafound/datasource/'
################################


def getURL(url, keyword):
    queryurl = url + keyword
    response = requests.get(queryurl)
    return response


def pubmedId(response):
    ID_container = []
    pubID = re.findall(r'from_uid=\d*', response)


    if(pubID != None):
        for item in pubID:
            ID_container.append(item[9:])

    return ID_container


def getsource(id):
    queryUrl = sourceUrl+id

    with open(path+'url.txt', 'a+') as f:
        f.write(queryUrl+'\n')

    response_source = requests.get(queryUrl).text
    return response_source


def savasource(path, source):
    """
    @:param
        Title
        Author
        Keywords
        Abstract
    """
    _title = re.findall(r'<title>.*', source)
    _title = str(_title)[9:-19]


    _auths = re.findall(r'<div class="auths">.*?</div>', source)
    _auths_list = re.findall(r'<a href=".*?">.*?</a>', str(_auths))

    authors_per_artical = []
    for per_auths in _auths_list:
        authors = re.findall(r'>.*?<', per_auths)
        authors_per_artical.append(str(authors)[3:-3])

    # print(authors_per_artical)

    _keywords = re.findall(r'<div class="keywords">.*?</div>', source)
    _keywords = re.findall(r'<p>.*</p>', str(_keywords))
    # print(_keywords)

    _abstract = re.findall(r'<div class="abstr">.*?</div>', source)
    _abstract = re.findall(r'<p>.*?</p>', str(_abstract))
    # print(str(_abstract[0])[3:-5])

    """
        Write file area
    """
    with open(path+'title.txt', "a+", encoding='utf-8') as fl:
        fl.write(str(_title) + '\n')

    with open(path+'keyword.txt', "a+", encoding='utf-8') as fl1:
        if len(_keywords) != 0:
            fl1.write(str(_keywords)[5:-7]+'\n')

        else:
            fl1.write('\n')

    with open(path + 'abstract.txt', "a+", encoding='utf-8') as fl2:
        if len(_abstract) != 0:
            fl2.write(str(_abstract[0])[3:-5] + '\n')
        else:
            fl2.write('\n')

    with open(path + 'authors.txt', "a+", encoding='utf-8') as fl3:
        if len(authors_per_artical) != 0:
            for i in range(len(authors_per_artical)-2):
                fl3.write(authors_per_artical[i] + ', ')
            fl3.write(authors_per_artical[-1] + "\n")

        else:
            fl3.write('\n')


if __name__ == "__main__":
    """
    keyword = "alternative splicing"  # for any keyword,don not run twice, the file is "a+"
    text = getURL(url, keyword).text
    ID_container = pubmedId(text)

    """
    source = getsource(ID_container[0])
    change = savasource(path, source)
    """

    savelist = ["title.txt", "keyword.txt", "abstract.txt", "authors.txt", "url.txt"]

    for name in savelist:
        with open(path + name, 'a+', encoding='utf-8') as f:
            f.write("<" + keyword + ">"+"\n")

    for item in ID_container:
        source = getsource(item)
        savasource(path, source)
    
    """


