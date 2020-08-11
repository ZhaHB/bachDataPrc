import csv
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


def getDataTag(pmid, tag):
    with open(tag, "r+", encoding='utf-8')as rfile:
        tagbuffer = ["id", "Gene", "Species", "Disease", "Chemical", "SNP", "DNAMutation", "CellLine"]

        tagarray = [[], [], [], [], [], [], [], []]
        tagarray[0].append(pmid)
        for line in rfile.readlines():
            if re.match(pmid, line):
                line = line.split('\t')
                # tagarray[0] = line[0]

                if len(line) > 2:

                    if line[2] in tagbuffer:
                        if line[1] not in tagarray[tagbuffer.index(line[2])]:
                            tagarray[tagbuffer.index(line[2])].append(line[1])

                    else:
                        pass

        tagdic = {}
        for item in tagarray:
            """
            if item is None:
                tagdic[tagbuffer[tagarray.index(item)]] = "null"

            elif len(item) == 1:
                tagdic[tagbuffer[tagarray.index(item)]] = item[0]
 
            else:
            """
            for i in item:
                tagdic[tagbuffer[tagarray.index(item)]] = i

        with open(_key + '_dataforKG.csv', 'a+', newline='')as f:
            fieldnames = {"id", "Gene", "Species", "Disease", "Chemical", "SNP", "DNAMutation", "CellLine"}
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            # writer.writeheader(columns=fieldnames)
            writer.writerow(tagdic)


if __name__ == "__main__":
    keyword = ["protein", "kinase", "disease", "fungus", "genetics", "neurobiology", "virology", "zoology"]

    for _key in keyword:
        with open(_key + '_dataforKG.csv', 'a+', newline='')as f:
            fieldnames = {"id", "Gene", "Species", "Disease", "Chemical", "SNP", "DNAMutation", "CellLine"}
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            # writer.writerow(tagdic)

        pmidfile = "../datasave/" + _key + "_pmid.pmid"
        nothingToWritefile = "../datasave/" + _key + "_nothting_to_write.txt"
        tagpath = "../dataforKG/" + _key + "_tag.txt"

        pmidBuffer = generatePreIDfile(pmidfile, nothingToWritefile)

        for pmid in pmidBuffer:
            getDataTag(pmid, tagpath)
