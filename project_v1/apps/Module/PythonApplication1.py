from . import Filter, InputProcess, SensitiveMap

#####處理input data#####

###導入評論(文本)###

filename = "apps/data/text.txt"
commentlist = []  # 每個element是一則評論
InputProcess.importtext(filename, commentlist)  # 欲比對評論

###建立詞彙森林###

# 導入三個database(positivewords, negativewords, and badwords)
# 統稱sensitivewords

positiveforest, negativeforest, badforest = (
    SensitiveMap.tree(),
    SensitiveMap.tree(),
    SensitiveMap.tree(),
)

filename = "apps/data/positivewords.txt"
InputProcess.buildforest(positiveforest, filename)

filename = "apps/data/negativewords.txt"
InputProcess.buildforest(negativeforest, filename)

filename = "apps/data/badwords.txt"
InputProcess.buildforest(badforest, filename)


#####印出詞彙森林#####

# print("positiveforest")
# positiveforest.printtree(0)

# print("negativewords")
# negativeforest.printtree(0)

# print("badwords")
# badforest.printtree(0)


#####印出欲比對的評論#####

# print("欲比對的評論")

# InputProcess. printcommentlist(commentlist)


#####開始分析評論#####

# Delete將評論分成好評, 壞評, 不雅, 中立
#!!!!!!!!!!!!!!!!
# comment_statistics = [0, 0, 0, 0]

###依序分析每則評論

resultlist_postive, resultlist_negative, resultlist_bad = [], [], []
# each element is Filter.Node()

for comment in commentlist:

    # list call by reference
    # 一則評論出現重複字彙只計一次，用flag判斷
    Filter.filter(positiveforest, comment, resultlist_postive, flag=True)
    Filter.filter(negativeforest, comment, resultlist_negative, flag=True)
    Filter.filter(badforest, comment, resultlist_bad, flag=True)

#####結果分析#####

# 計算正面、負面、不雅詞彙個別最頻繁使用的詞彙
# 計算正面、負面、不雅詞彙個別最頻繁使用的詞彙
highfrgy_postive = []
highfrgy_negative = []
highfrgy_bad = []
# 計算正面、負面、不雅詞彙各別累加的分數(3個分數)
score = [0, 0, 0]  # order: positive>negative>bad
# 計算正面、負面、不雅詞彙個別使用次數
cnt = [0, 0, 0]  # order: positive>negative>bad

Filter.calculate(
    resultlist_postive,
    resultlist_negative,
    resultlist_bad,
    highfrgy_postive,
    highfrgy_negative,
    highfrgy_bad,
    score,
    cnt,
)

# 計算使用多少次sensitive words(正面+負面+不雅詞彙使用次數)
totalcnt = Filter.cntsenswords(cnt)

# 印出使用多少次sensitive words
print("Sensitive words使用次數：", totalcnt)
print("\n")

# 印出正面、負面、不雅詞彙各別累加的分數(3個數字)
print("正面詞彙分數：", score[0])
print("負面詞彙分數：", score[1])
print("不雅詞彙分數：", score[2])
print("\n")

# 印出正面、負面、不雅詞彙各個使用次數
print("正面詞彙使用次數：", cnt[0])
print("負面詞彙使用次數：", cnt[1])
print("不雅詞彙使用次數：", cnt[2])
print("\n")

# 印出正面、負面、不雅詞彙每個使用到的詞彙
print("正面詞彙")
Filter.printresultlist(resultlist_postive)
print("負面詞彙")
Filter.printresultlist(resultlist_negative)
print("不雅詞彙")
Filter.printresultlist(resultlist_bad)
print("\n")

# 印出正面、負面、不雅詞彙個別最頻繁使用的詞彙

print("最高頻率出現的正面詞彙：")
Filter.printhighfrgy(highfrgy_postive)
print("最高頻率出現的負面詞彙：")
Filter.printhighfrgy(highfrgy_negative)
print("最高頻率出現的不雅詞彙：")
Filter.printhighfrgy(highfrgy_bad)


# 信用度評分
# 正面詞彙分數/負面詞彙分數

print("信用度：", end=" ")

if score[1] == 0:
    ratio = 3
else:
    # ratio = score[0] / score[1]
    ratio = score[0] / (score[0] + score[1] + score[2])

print(ratio)

if ratio >= 3:
    print("優良")
elif ratio >= 2:
    print("良")
elif ratio >= 1:
    print("普通")
else:
    print("不優")


# 整理為 [分數, 次數, words] 格式
positive_dataset = Filter.result_tidy(resultlist_postive)
negative_dataset = Filter.result_tidy(resultlist_negative)
bad_dataset = Filter.result_tidy(resultlist_bad)

###################################################
# 以下為傳到 app.py 變數設定
# 存成一個字典送過去

# app.py:
# details=PA1.data_details

# html 接收
# {{ details.positive }}
data_details = {
    "total_count": totalcnt,  # 總次數
    "positive_count": cnt[0],
    "negative_count": cnt[1],
    "bad_count": cnt[2],
    "positive_score": score[0],  # 分數
    "negative_score": score[1],
    "bad_score": score[2],
    "star": ratio,  # 星星
}
