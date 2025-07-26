def Fibanacii(num):
    if(num <= 1):
        return num
    else:
        return Fibanacii(num-1) + Fibanacii(num-2)
    
print(Fibanacii(8))
