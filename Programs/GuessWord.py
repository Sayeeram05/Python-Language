import random   # Used this library to generate random number

print('''\n----------- Lets play Word Guessing game ! ----------- 
    \n\n
    How to Play ?
        1.Progarm will randomly select the word from the list
        2.You have to guess that Word\n''')

WordList = ["house","dog","cat","table","chair","book","phone","food","water","sleep"]

RandomWord = WordList[(random.randint(0,10))]   # Stores a random word form the list using random index 0-9
Attempts = 1

while True:
    print("Word List = ",end="")    
    print(*WordList,sep=",")    # print the Word List

    UserGuessed = input("\nEnter the Word From Word List (above) : ")
    
    if(UserGuessed not in WordList):
        print("\nEnter The Word Form the List")
    elif(RandomWord == UserGuessed.lower()):
        print(f"\nWell Done !!!\nAttempts = {Attempts}")
        break
    else:
        print("\nWrong Guess")
        Attempts += 1




