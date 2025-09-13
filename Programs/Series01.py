Length = int(input("Number :  "))

print("Series : ",end="")
i = 0
j = 1
count = 0
while(count < Length):
    
    if(i != 0 and i % 10 == 0):
        i += 2
        continue
    j += i
    print(j,end=" ")
    i += 2
    count += 1
    


    