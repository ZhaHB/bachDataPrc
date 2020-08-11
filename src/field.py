def generateFieldsSQL(main_area, main_area_Eng):
    countNum = len(main_area)
    idBuff = []

    for i in range(countNum):

        id = (i + 1) * 10

        countDigit = len(str(id))
        hasToAdd = 5 - countDigit

        generateid = hasToAdd * "0" + str(id)

        idBuff.append(generateid)
    with open("../SQLgenerate/Field.txt", "w+", encoding='utf-8')as readfile:
        for i in range(len(main_area)):
            readfile.write("INSERT INTO `fields` VALUES (" + "\'" + idBuff[i] + "\'" + ", " + "\'" + main_area[i] + "\'" + ", " + "\'" +main_area_toEng[i] + "\'" + ");\n")


if __name__ == "__main__":
    main_area = ["基因组学", "细胞学", "生物化学与分子生物学", "植物学", "动物学", "神经生物学", "遗传学", "病毒学", "细菌生物学", "真菌学", "疾病"]
    main_area_toEng = ["gene", "cell", "biochemistry and molecular biology", "botany", "zoology", "neurobiology", "genetics", "virology", "bacteriology", "fungus", "disease"]

    generateFieldsSQL(main_area, main_area_toEng)
