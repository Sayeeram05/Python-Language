if __name__ == '__main__':
    Data = []
    ScoreList =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Data.append([name,score])
        ScoreList.append(score)
    Data.sort()
    ScoreList = list(set(ScoreList))
    ScoreList.sort()
    for i in Data:
        if(i[1] == ScoreList[1]):
            print(i[0])
