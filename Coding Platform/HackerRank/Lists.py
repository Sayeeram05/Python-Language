if __name__ == '__main__':
    Data = []
    N = int(input())
    for i in range(N):
        S = input().split()
        if(S[0] == "insert"):
            Data.insert(int(S[1]),int(S[2]))
        elif(S[0] == "print"):
            print(Data)
        elif(S[0] == "remove"):
            Data.remove(int(S[1]))
        elif(S[0] == "append"):
            Data.append(int(S[1]))
        elif(S[0] == "sort"):
            Data.sort()
        elif(S[0] == "pop"):
            Data.pop()
        elif(S[0] == "reverse"):
            Data.reverse()
            