"""
@Time       : 2020/9/8 19:21
@FileName   : 09_08test01.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test01():
    wordList = []
    flag = 0
    sensiWord = input().strip()
    doulen = 0
    arr = input().strip()
    if "," in arr:
        flag = 1
        arr = arr.split(",")
        doulen = len(arr)
        for i in range(doulen):
            wordList.extend(arr[i].split(" "))
            # wordList.extend(arr[1].split(" "))
        # halfArr = len(arr[0].split(" "))

    else:
        flag = 0
        halfArr = 0
        wordList.extend(arr.split(" "))
    replace = input().strip()

    # print(arr[0])
    # print(wordList)
    words = [0] * 26
    for i in range(len(sensiWord)):
        words[ord(sensiWord[i]) - ord('a')] += 1
    # print(wordList)
    for i in range(len(wordList)):
        if len(wordList[i]) == len(sensiWord):
            if jack(words[:], wordList[i]):
                wordList[i] = replace
    # print(wordList)
    res = ""
    start = 0
    end = 0
    if flag:
        for i in range(doulen):
            end += len(arr[i].split(" "))
            res += " ".join(wordList[start:end]) + ","
            start = end
    else:
        res += " ".join(wordList) + ","
    res = res[:-1]
    if ord("z") >= ord(res[-1]) >= ord("a"):
        print(res)
    else:
        print(res[:-1])

    # return " ".join(wordList[:halfArr]) + "," + " ".join(wordList[halfArr:]) \
    #     if flag else " ".join(wordList)


def jack(words, word):
    for i in range(len(word)):
        words[ord(word[i]) - ord('a')] -= 1
    return True if sum(words) == 0 else False


if __name__ == '__main__':
    res = test01()
    # print(res)
