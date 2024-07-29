import random # Module

#------------------------------------ Function ------------------------------------#
def PlayerTurn():
    global PlayerChoice
    print('''\nEnter choice 
    1. Rock 
    2. paper 
    3. scissor ''')
    while True:
        PlayerChoice = input("Player Turn (1/2/3): ")
    
        if(PlayerChoice not in ['1','2','3']):
            print("\nInvalid Choice\n")
        else:
            break
    if(PlayerChoice == '1'):
        PlayerChoice = "rock"
    elif(PlayerChoice == '2'):
        PlayerChoice = "paper"
    elif(PlayerChoice == '3'):
        PlayerChoice = "Scissor"

    print("\nplayer choice is :",PlayerChoice)

    print("\nNow its computer turn.......")

#------------------------------------ Main ------------------------------------#

print('''
⭐ Welcome to the Rock-Paper-Scissors Game! ⭐

How to Play❓
1. You will play against the computer.
2. Both you and the computer will choose either Rock, Paper, or Scissors.
3. The choices are compared, and the winner is decided based on the following rules:
    - rock vs paper -> paper wins 
    - rock vs scissors -> rock wins 
    - paper vs scissors -> scissors wins 
4. If both choose the same, it's a tie, and you play again.

Let's Start! ⭐👍
''')

Computer_win = 0
Player_win = 0

while True:
    #------------------------------------ Player ------------------------------------#

    PlayerTurn() # Player

    #------------------------------------ Computer ------------------------------------#

    Choice_List = ["Scissor","rock","paper"]
    ComputerChoice = random.choice(Choice_List)

    print("\nComputer choice is :",ComputerChoice)

    print(f"{PlayerChoice} V/S {ComputerChoice}")

    if(PlayerChoice != ComputerChoice):
        if((PlayerChoice == "Scissor" or PlayerChoice == "paper") and (ComputerChoice == "Scissor" or ComputerChoice == "paper")):
            if(PlayerChoice == "Scissor"):
                print(f"\nPlayer Won the game - {PlayerChoice}")
                Player_win +=1
            else:
                print(f"\nComputer Won the game - {ComputerChoice}")
            Computer_win += 1
        elif(Choice_List.index(ComputerChoice) > Choice_List.index(PlayerChoice)):
            print(f"\nComputer Won the game - {ComputerChoice}")
            Computer_win += 1
        else:
            print(f"\nPlayer Won the game - {PlayerChoice}")
            Player_win += 1

        print(f"Computer Won : {Computer_win}\nPlayer Won : {Player_win}")

        Next = input("\nDo you want to play again? (y/n) : ").lower()

        if(Next == 'y'):
            print("\nLets Play Alother Game")
        else:
            print("\nThanks For The Game")
            break
    else:
        print("\nSame Guess! \n Let's Play another game \n")

