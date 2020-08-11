keywordbuffer = ["bacteriology", "botany", "cell", "disease", "fungus", "gene", "genetics", "kinase", "neurobiology", "protein", "virology", "zoology"]

for keyword in keywordbuffer:

    absPath = "../SdataN_46/" + keyword + "_abs.txt"
    titlePath = "../SdataN_46/" + keyword + "_title.txt"

    with open(absPath, "r+", encoding='utf-8')as rfile:
        with open("../S/" + keyword + "_abs.txt", "a+", encoding='utf-8')as wfile:
            for line in rfile.readlines():
                line = line.replace("\'", str(" \\' "))

                wfile.write(line)

    with open(titlePath, "r+", encoding='utf-8')as _rfile:
        with open("../S/" + keyword + "_title.txt", "a+", encoding='utf-8')as _wfile:
            for _line in _rfile.readlines():
                _line = _line.replace("\'", str(" \\' "))

                _wfile.write(_line)

