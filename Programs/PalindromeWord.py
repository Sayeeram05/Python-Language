print("------------- Palindrome Word -------------")

Word = input("Enter Word : ")

check = ""

print("Method 1 : ")
check = Word[-1::-1]
if(check == Word):
    print(f"{Word} is Palindrome")
else:
    print(f"{Word} is not Palindrome")

print("Method 2 :")
L = len(Word) 
for i in range(L // 2):
    if(Word[i] != Word[L-i-1]):
        print(f"{Word} is not Palindrome")
        break
else:
    print(f"{Word} is Palindrome")
    
print("Method 3 :")
L = len(Word) // 2
if(Word[:L] == Word[-1:L:-1]):
    print(f"{Word} is Palindrome")
else:
    print(f"{Word} is not Palindrome")