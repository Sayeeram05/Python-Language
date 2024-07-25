import os,time  #os module to clear screen and time module to sleep the screen

print('''-------- Welcome To Master Game--------\n\n
How To Play ?
    1.First Player 1 Have To Enter A Number
    2.Then Player 2 Have To Find That Number
\n\n Let's Start 👍''')

if(__name__ == '__main__'): # Runs Only in this File (print(__name__))
    
    while True : # if Player 1 entered invalid inputs

        Player1 = input("\nPlayer 1 Enter the Number : ")  # string for slicing the number and check with player 2

        length  = len(Player1)  # length of player 1

        if(Player1.isdigit()): # checks the player1 entered a number or not
            time.sleep(1)   # sleep for 1 second
            os.system('cls')  # clear the terminal

            Player2attempts = 1   # to Count the Player2 attempts

            while True:    # if Player 2 entered invalid inputs

                correct = 0  # to check how many digits player 2 gussed correctly

                Player2 = input(f"\n\nPlayer 2 Guess the {length} digit Number Player 1 Entered : ")

                if(Player2.isdigit() and len(Player2) == length):   # checks the player 2 entered a number or not and checks length of player 1 and player 2 digits

                    print("\n\tPlayer 1 Entered : ",end="")

                    for i in range(0,length):  # to check the digits one by one

                        if(Player1[i] == Player2[i]):
                            print(Player1[i],end=" ")
                            correct = correct + 1
                        else:
                            print("X",end=" ")
                            
                    Player2attempts += 1
                    
                    if(correct == length):

                        if(Player2attempts == 1):
                            print("\n\n👌 Great! You guessed the number in just 1 try! You're a Mastermind!")
                        else:
                            print(f"\nWell Done 👌 You guessed the number in {Player2attempts} Try!")

                        break # breaks the Player 2 while  loop
                else:

                    print("\n❌ Player 2 Invalid Number")

            break   # breaks the Player 1 while  loop

        else:
                print("\n❌ Player 1 Invalid Number")
            
    