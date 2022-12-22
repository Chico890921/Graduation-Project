class Node:
    def __intit__(self):
        self.value = "\0"
        self.score = 0
        self.cnt = 1  # 使用次數


def insert_resultlist(flag, resultlist, result_node):

    # 存不存在resultlist中
    for node in resultlist:
        # 存在，一則評論出現重複字彙只計一次，用flag判斷
        if result_node.value == node.value:
            if flag:
                node.cnt += 1
                flag = False
            return

    # 不存在，放入
    resultlist.append(result_node)


def filter(forest, text, resultlist, flag):

    curlevel = forest
    record = []

    # 遍歷文本
    for w in text:

        curnode = None
        end = False

        # 遍歷curlevel.nodelist，w是否在nodelist中
        for node in curlevel.nodelist:
            if w == node.value:
                curnode = node
                # 如果下一個是數字，代表該詞彙已結尾
                nextvalue = curnode.childtree.nodelist[0].value

                if nextvalue.isdigit():
                    end = True
                """
                isdigit()
                True: Unicode數字，byte數字(單字節)，全角數字(雙字節)，羅馬數字
                False: 漢字數字
                Error: 無

                isdecimal()
                True: Unicode數字，全角數字(雙字節)
                False: 羅馬數字， 漢字數字
                Error: byte數字(單字節)

                isnumeric()
                True: Unicode數字，全角數字(雙字節)，羅馬數字， 漢字數字
                False: 無
                Error: byte數字(單字節)
                """

        # 如果都沒有找到
        if curnode == None:
            record = []  # 清除
            curlevel = forest  # 回到最上層
        # 如果已經到結尾
        elif end:
            # 紀錄這個字
            record.append(w)

            result_node = Node()
            result_node.value = record

            result_node.score = int(nextvalue)
            result_node.cnt = 1  #!!宣告
            insert_resultlist(flag, resultlist, result_node)

            record = []
            curlevel = forest  # 回到最上層，換新的詞
        # 如果還沒到結尾，代表該詞彙還不完整
        else:
            record.append(w)
            curlevel = curnode.childtree

    # 分析的結果紀錄在resultlist


#####Result Analysis#####

# 計算正面、負面、不雅詞彙個別使用次數
def cntwords(node):

    return node.cnt


# 計算正面、負面、不雅詞彙各別累加的分數(3個分數)
def addscore(node):

    return node.score * node.cnt


# 計算正面、負面、不雅詞彙個別最頻繁使用的詞彙
# 可能不只一個，可能遇到使用次數相同的兩個詞彙
def frequency(frqylist, node):
    if len(frqylist) == 0:
        frqylist.append(node)
    # 取代
    elif node.cnt > frqylist[0].cnt:
        frqylist.clear()  # 清空
        frqylist.append(node)
    # 加入
    elif node.cnt == frqylist[0].cnt:
        frqylist.append(node)


def calculate(
    resultlist_postive,
    resultlist_negative,
    resultlist_bad,
    highfrgy_postive,
    highfrgy_negative,
    highfrgy_bad,
    score,
    cnt,
):

    """
    #計算正面、負面、不雅詞彙個別最頻繁使用的詞彙
    highfrgy_postive = []
    highfrgy_negative = []
    highfrgy_bad = []
    #計算正面、負面、不雅詞彙各別累加的分數(3個分數)
    score = [0, 0, 0] # order: positive>negative>bad
    #計算正面、負面、不雅詞彙個別使用次數
    cnt = [0, 0, 0] # order: positive>negative>bad
    """

    for node in resultlist_postive:
        # 計算正面、負面、不雅詞彙各別累加的分數(3個分數)
        score[0] += addscore(node)
        # 計算正面、負面、不雅詞彙個別最頻繁使用的詞彙
        frequency(highfrgy_postive, node)
        # 計算正面、負面、不雅詞彙個別使用次數
        cnt[0] += cntwords(node)

    for node in resultlist_negative:
        # 計算正面、負面、不雅詞彙各別累加的分數(3個分數)
        score[1] += addscore(node)
        # 計算正面、負面、不雅詞彙個別最頻繁使用的詞彙
        frequency(highfrgy_negative, node)
        # 計算正面、負面、不雅詞彙個別使用次數
        cnt[1] += cntwords(node)

    for node in resultlist_bad:
        # 計算正面、負面、不雅詞彙各別累加的分數(3個分數)
        score[2] += addscore(node)
        # 計算正面、負面、不雅詞彙個別最頻繁使用的詞彙
        frequency(highfrgy_bad, node)
        # 計算正面、負面、不雅詞彙個別使用次數
        cnt[2] += cntwords(node)


# 計算使用多少次sensitive words(正面+負面+不雅詞彙使用次數)
def cntsenswords(cnt):
    totalcnt = 0
    for i in cnt:
        totalcnt += i

    return totalcnt


def printhighfrgy(highfrgy):
    for node in highfrgy:
        print(node.value, node.cnt, "次")


def printresultlist(resultlist):

    for node in resultlist:
        print(node.value, "分數：", node.score, "次數：", node.cnt)


# 整理為 [分數, 次數, words] 格式
def result_tidy(resultlist):
    dataset = {}
    dataset["source"] = []
    dataset["source"].append(["score", "amount", "product"])
    for node in resultlist:
        dataset["source"].append([node.score, node.cnt, str(node.value)])

    return dataset
