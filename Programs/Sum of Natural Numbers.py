def SumN(num):
    if num == 1:
        return 1
    else:
        return num + SumN(num-1)
    
print(SumN(5))