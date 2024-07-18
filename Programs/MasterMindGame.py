import random

Digit = random.randint(3,6)

Number = ""

for i in range(0,Digit):
    Number += str(random.randint(0,9))

print('''
⭐ Welcome to the Master Mind Game! ⭐

How to Play❓
1. The computer sets a multi-digit number.
2. You try to guess the number.
3. If you guess correctly on your first try, you win and are crowned Mastermind! If not, the computer gives hints about which digits you got correct.
4. Keep guessing until you guess the entire number correctly.
5. Then, you get to set a number and the computer will try to guess it.
6. If the computer guesses your number in fewer attempts than you took, the computer wins. If not, you win!

Let's Start! ⭐👍
''')

Correct = 0
Attempt = 0
print(Number)

while True:
    Guessed_Number = input(f"\nGuess the {Digit} digit number : ")
    Attempt += 1
    if(len(Guessed_Number) != len(Number)):
        print(f"\nWrong Guess.\nYou Only Enterd {len(Guessed_Number)}-Digts insted of {Digit}-Digits")
        continue
    temp = ""
    if(Number == Guessed_Number):
        print("\nYou've become a Mastermind")
        if(Attempt == 1):
            print("\nGreat! You guessed the number in just 1 try!👍 \n")
            break
        else:
            print(f"\nGreat! It took you only {Attempt} tries.\n")
            break
    else :
        for i,j in zip(Number,Guessed_Number): # zip - combines to iterable data types [[1,1],[2,3],[4,5]]
            if(i == j):
                temp += j
                Correct += 1
            else:
                temp += "_"

        print(f"\nNot quite the number. But you did get {Correct} digit(s) correct!")
        print("Also these numbers in your input were correct.")
        print(temp)
        