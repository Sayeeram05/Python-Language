num = int(input("Number : "))

for i in range(num+1):
    if(i == 0):
        print(str("*").center(50))
    else:
        s = "*"
        s += (i*2 -1)*" "
        s += ("*")
        print(s.center(50))
        
for i in range(num,-1,-1):
    if(i == 0):
        print(str("*").center(50))
    else:
        s = "*"
        s += (i*2 -1)*" "
        s += ("*")
        print(s.center(50))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  