
def getName(tagpath, buffer):
    with open(tagpath, "r+", encoding="utf-8")as rfile:
        for line in rfile.readlines():
            line = line.split('\t')
            if len(line) > 2:
                if line[2] == tag:
                    if line[1] not in buffer:
                        buffer.append(line[1])

            else:
                pass


def wfile():
    with open("../dforT/" + tag + ".txt", "w+")as wcfile:

        for i in wordbuffer:
            wcfile.write(i + "\n")


if __name__ == "__main__":
    wordbuffer = []
    tag = "CellLine"

    keyword = ["cell", "protein", "bacteriology", "kinase", "disease", "botany", "fungus", "genetics", "neurobiology", "virology", "zoology"]
    for item in keyword:

        tagpath = "../dataforKG/" + str(item) +"_tag.txt"

        getName(tagpath, wordbuffer)

    # print(len(wordbuffer))

    genebuffer = []

    with open("../dataforKG/gene_tag.txt", "r+", encoding="utf-8")as gfile:
        for _line in gfile.readlines():
            _line = _line.split('\t')
            if len(_line) > 2:
                if _line[2] == tag:
                    if _line[1] not in genebuffer:
                        genebuffer.append(_line[1])

    for _item in genebuffer:
        if _item in wordbuffer:
            wordbuffer.remove(_item)

    wfile()
