def getNoRfile(readfile, kwd):
    idBuff = []
    # repeatbuff = []

    with open(str(kwd)+"_ex.pmid", "w+") as wfile:
        with open(readfile, 'r+')as rfile:
            for item in rfile:
                item = item.replace("\n", "")

                if item not in idBuff:
                    idBuff.append(item)

                else:
                    pass

        for id in idBuff:
            wfile.write(id + "\n")


#if __name__ == "__mian__":

keyword = ["botany", "fungus", "genetics", "neurobiology", "virology", "zoology"]

for kwd in keyword:
    readfile = str(kwd) + "_pmid.pmid"

    getNoRfile(readfile, kwd)