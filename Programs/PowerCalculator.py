def Pow(num,pow):
    if(pow == 0):\
        return 1
    if(pow == 1):
        return num
    else:
        return num * Pow(num,pow-1)
    
print(Pow(3,4))
print(Pow(5,0))