a = 0
b = 1
n = int(input("Enter the length of fibonacci series : "))
if(n>=1):
    print(a,end=" ")
if(n>=2):
    print(b,end=" ")
for i in range(n-2):
    c = a + b;
    print(c,end=" ")
    a = b
    b = c