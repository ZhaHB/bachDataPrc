import re

import requests


##################################
sourceUrl = "https://www.ncbi.nlm.nih.gov/pubmed/"
####################################


def _generatePreIDfile(pmidfile, nothingToWritefile):
    # 缓存buffer
    nothingToWritefilebuffer = []

    pmidfilebuff = []

    with open(nothingToWritefile, "r+", encoding="utf-8")as rfile:
        for line in rfile.readlines():
            line = line.replace("\n", "")
            nothingToWritefilebuffer.append(line)

    with open(pmidfile, "r+", encoding="utf-8")as _rfile:
        for _line in _rfile.readlines():
            _line = _line.replace("\n", "")
            pmidfilebuff.append(_line)

    # print(len(pmidfilebuff))

    for item in nothingToWritefilebuffer:
        if item in pmidfilebuff:
            pmidfilebuff.remove(item)

    """
    with open(path + keyword + "_ge_pid.txt", 'w+', encoding='utf-8') as wfile:
        for item in pmidfilebuff:
            wfile.write(item + "\n")
    """

    return pmidfilebuff


def _getsource(id):
    queryUrl = sourceUrl + id

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

    """
    _title = re.findall(r'<title>.*', source)
    _title = str(_title)[9:-19]
    """

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

    """
    _abstract = re.findall(r'<div class="abstr">.*?</div>', source)
    _abstract = re.findall(r'<p>.*?</p>', str(_abstract))
    """

    # print(str(_abstract[0])[3:-5])

    """
        Write file area
    """
    # with open(path + keyword + '_title.txt', "a+", encoding='utf-8') as fl:
        # fl.write(str(_title) + '\n')

    with open(path + keyword + '_keyword.txt', "a+", encoding='utf-8') as fl1:
        if len(_keywords) != 0:
            fl1.write(str(_keywords)[5:-7]+'\n')

        else:
            fl1.write('\n')

    """
    with open(path + keyword + '_abstract.txt', "a+", encoding='utf-8') as fl2:
        if len(_abstract) != 0:
            fl2.write(str(_abstract[0])[3:-5] + '\n')
        else:
            fl2.write('\n')
    """

    with open(path + keyword + '_authors.txt', "a+", encoding='utf-8') as fl3:
        if len(authors_per_artical) != 0:
            for i in range(len(authors_per_artical)-2):
                fl3.write(authors_per_artical[i] + ', ')
            fl3.write(authors_per_artical[-1] + "\n")

        else:
            fl3.write('\n')


path = "../dataN_46/"
keyword = "cell"

pmidfile = "../datasave/" + keyword + "_pmid.pmid"

nothingToWritefile = "../datasave/" + keyword + "_nothting_to_write.txt"

_pmidBuffer = _generatePreIDfile(pmidfile, nothingToWritefile)

# print(_pmidBuffer)

for id in _pmidBuffer:

    source = _getsource(id)
    savasource(path, source)

