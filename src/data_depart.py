"""
@:parameter
    arraylist
    abr: abs for all the text file
"""


filepath = "C:/Users/asus/Desktop/Datafound/datasource/abstract.txt"
stopword_filepath = "C:/Users/asus/Desktop/Datafound/datasource/stopword.txt"


def wordSplit(path):
    listBuffer = []
    with open(path, 'r+', encoding="UTF-8") as filebuffer:
        for readline in filebuffer:
            listBuffer.append(readline.split(' '))

    return listBuffer


def stoplistcontr(stopword_path):
    bufferlist = []
    bufferitem = []
    with open(stopword_path, 'r+', encoding="UTF-8") as stopBuffer:
        for readline in stopBuffer:
            bufferlist.append(readline.split())
    for listitem in bufferlist:
        for item in listitem:
            bufferitem.append(item)

    return bufferitem


def stopwordDelete(stopwordbuf, readlineBuffer):
    BcForRBuffer = []
    for readlines in readlineBuffer:
        for stopword in stopwordbuf:
            for keyword in readlines:
                if keyword.lower() == stopword:
                    # print(keyword)
                    readlines.remove(keyword)
        BcForRBuffer.append(readlines)
    return BcForRBuffer


def wordprocess(processList):

    return None


if __name__ == "__main__":
    """
    listbuf = wordSplit(filepath)
    print(len(listbuf))
    """
    readlineBuffer = wordSplit(filepath)
    stopwordBuf = stoplistcontr(stopword_filepath)
    process_wordlist = stopwordDelete(stopwordBuf, readlineBuffer)

    for item in process_wordlist:
        print(item)

