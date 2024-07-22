import random
    
print('''
⭐ Welcome to the Cows and Bulls Game! ⭐

How to Play❓
1. The computer will create a secret 4-digit code with no repeated digits.
2. You will try to guess the secret code.
3. After each guess, you will receive two hints:
   - Bulls: Number of correct digits in the correct position.
   - Cows: Number of correct digits in the wrong position.
4. For example, if the secret code is 1234 and your guess is 1246, you get:
   - 2 Bulls (digits 1 and 2 in the correct positions)
   - 1 Cow (digit 4 in the wrong position)
5. Keep guessing until you crack the secret code. The player who guesses the code in the fewest attempts wins.

Let's Start! ⭐👍
''')

Secret_Code = random.randint(1000,9999)
# print(Secret_Code)

while True:
    Cows,Bulls = 0,0
    try : 
        Player_Guess = int(input("Guess : "))

        if(Player_Guess >= 1000 and Player_Guess <= 9999):
            if(Player_Guess == Secret_Code):
                print("\nYou guessed right!\n")
                break
            else:
                for i in range(4):
                    if(str(Player_Guess)[i] == str(Secret_Code)[i]):
                        Bulls += 1
                    else:
                        Cows += 1
                print(f"Response: {Bulls} Bulls, {Cows} Cows")
        else:
            print("\nInvalid Digit(only 4 Digit)\n")
    except :
        print("\nInvalid Number\n")


