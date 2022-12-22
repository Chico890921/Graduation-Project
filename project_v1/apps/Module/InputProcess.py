from . import SensitiveMap


def importtext(filename, textlist):
    file = open(filename, "r", encoding="utf-8")  # encoding="utf-8"
    text = ""
    for line in file.readlines():

        # 每則評論以 區分

        if line == "結束\n" or line == "結束" or line == "\n":
            textlist.append(text)
            text = ""
        else:
            text += line

    file.close()


def importwords(filename, wordslist):

    file = open(filename, "r", encoding="utf-8")

    for line in file.readlines():  # 依次read line
        line = line.strip()  # 去除每行頭尾空白
        wordslist.append(line)
    file.close()


def buildforest(self, filename):

    wordslist = []
    importwords(filename, wordslist)
    self.insertword(wordslist)


def printcommentlist(commentlist):
    tmp = 0
    for comment in commentlist:
        tmp += 1
        print("第", tmp, "則評論：")
        print(comment)
