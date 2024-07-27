import random

print('''
⭐ Welcome To Number Gussing Game ⭐
    
How To Play❓
    1.Computer Randomly choose a number between 0 - 10
    2.Player have to guess the number

Let's Start⭐👍   
''')

Random_Number = random.randint(0,10)

Attempt = 1

while(True):
    try:
        Guess_number = int(input("Enter The Gussed Number(0-10) : "))
    except:
        print("Invalid Number\n")
        continue
    
    if(Guess_number >= 0 and Guess_number <= 10):
        if(Guess_number == Random_Number):
            print(f"Correct Guess in {Attempt} Attempt\n")
            break
        else:
            print("Try In Next Attempt\n")
            Attempt += 1
    else:
        print("Gussed Number isn't Between 0 and 10\n")


print("\n\n Thanks For Playing 👍")

