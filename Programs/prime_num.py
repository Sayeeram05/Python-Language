for i in range(1,4):   
    try:
        a = int(input("Enter a number to check prime or not : "))
    except ValueError:
        raise ValueError("Enter a positive integer")
    check = 0
    if(a==1 or a==0):
        check=1
        print(a,"is not a prime")
        break
    elif(a>1):
        for i in range(1,a):
            if(a%i==0):
                print(a,"is not a prime")
                check = 1
                break
        break
    elif(a<0):
        check=1
        print("Invalid number")
    if(check==0):
        print(a,"is a prime");
        break