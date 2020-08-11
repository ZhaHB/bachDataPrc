import re


def generatePreIDfile(pmidfile, nothingToWritefile):
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

    return pmidfilebuff


def findEntity(pubtator_file, pmidBuffer, titlesave, absave, pubtatorsave):
    with open(pubtator_file, "r+", encoding="utf-8")as rfile:
        with open(titlesave, "a+", encoding='utf-8')as titlefile:
            with open(absave, "a+", encoding='utf-8')as absfile:
                with open(pubtatorsave, "a+", encoding='utf-8')as pubfile:
                    for line in rfile.readlines():
                        for _item in pmidBuffer:
                            _item = str(_item)
                            if re.match(_item, line):
                                linesign = line[0:11]
                                if linesign == _item + "|t|":
                                    if len(line) > 13:
                                        # print(line[11:])
                                        titlefile.write(line[11:])
                                    else:
                                        titlefile.write(_item + " is null" + "\n")

                                elif linesign == _item + "|a|":
                                    if len(line) > 13:
                                        # print(line[11:])
                                        absfile.write(line[11:])
                                    else:
                                        absfile.write(_item + " is null" + "\n")

                                else:
                                    linetest = line.replace("\n", "")
                                    linebuffer = linetest.split("\t")
                                    linebuffer = linebuffer[0:1] + linebuffer[3:]

                                    for i in linebuffer:
                                        # print(i)
                                        pubfile.write(i + "\t")

                                    pubfile.write("\n")

                            else:
                                pass


keyword = ["cell"]

for item in keyword:
    # file path definition area
    pmidfile = "../datasave/" + str(item) + "_pmid.pmid"
    nothingToWritefile = "../datasave/" + str(item) + "_nothting_to_write.txt"
    pubtator_file = "../datasave/" + str(item) + "_pubtator.txt"

    titlesave = "../dataforKG/" + str(item) + "_title.txt"
    absave = "../dataforKG/" + str(item) + "_abs.txt"

    pubtatorsave = "../dataforKG/" + str(item) + "_tag.txt"

    pmidBuffer = generatePreIDfile(pmidfile, nothingToWritefile)

    # print(pmidBuffer)

    """
    findEntity(pubtator_file, pmidBuffer, titlesave, absave, pubtatorsave)
    """
