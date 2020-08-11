def getpaperID(filePath):
    idBuffer = []
    with open(filePath, 'r+', encoding="utf-8") as readfile:
        for _id in readfile.readlines():
            _id = _id.replace("\n", "")
            idBuffer.append(_id)

    return idBuffer


def generatetagSQL(bufferID, keyword):
    with open("../sSQLgenerate/New_tag.txt", "a+", encoding="utf-8") as addfile:
        for paperID in bufferID:
            addfile.write("INSERT INTO `paper_tag` VALUES (" + "\'" + str(paperID) + "\'" + ", " + "\'" + keyword + "\'" + ");\n")


#################################################################

keywordbuffer = ["bacteriology", "botany", "cell", "disease", "fungus", "gene", "genetics", "kinase", "neurobiology", "protein", "virology", "zoology"]

for keyword in keywordbuffer:

    filePath = "../sdataN_46/" + keyword + "_ge_pid.txt"

    bufferID = getpaperID(filePath)

    generatetagSQL(bufferID, keyword)


