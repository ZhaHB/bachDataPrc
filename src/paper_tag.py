from src.author_paperSQL import getPID


def generatePaperTagSQL(paperID, main_area_toEng):
    pass


def detectRepeatItem(paperid):
    storeBuff = []
    indexBuff = []
    repeateditem = []

    for item in paperid:
        if item not in storeBuff:
            storeBuff.append(item)

        else:
            indexBuff.append(paperid.index(item))
            repeateditem.append(item)

    print(len(indexBuff))


if __name__ == "__main__":
    ###############################
    #   defined source
    ###############################
    articleUrl = "../datasource/url.txt"
    main_area_toEng = ["gene", "cell", "biochemistry and molecular biology", "botany", "zoology", "neurobiology", "genetics", "virology", "bacteriology", "fungus", "disease"]

    ####################################
    #   Data Interface
    ###################################
    paperID = getPID(articleUrl)

    detectRepeatItem(paperID)

    # generatePaperTagSQL(paperID, main_area_toEng)
