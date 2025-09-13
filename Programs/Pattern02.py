i = 1
Check = True
while i != 0:
    Temp = [0]*5
    if(i == 1):
        Temp[i-1] = Temp[-1] = 1
    elif(i <= 3):
        for j in range(i-1,5,i):
            Temp[j] = i
    if(i == 3):
        Check = False
    if(Check == False):
        i -= 1
    else:
        i += 1
    print(Temp)
