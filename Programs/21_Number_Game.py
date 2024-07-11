import random
def Computer_Turn():
    
    global Number_21,Game

    Count = random.randint(1,5)

    
    if(len(Number_21) == 0):
        for i in range(1,Count+1):
            Number_21.append(i)
        

    elif(Number_21[-1] == 20):
        print("\nPlayer Won the Game")
        Game = False
        return

    elif((Number_21[-1] + Count) >= 21 and (Number_21[-1] <= 19)):
        for i in range(1,Count):
            if((Number_21[-1] + i + 1) == 21 ):
                Count = i
                # print("Count :",Count)
                break
        for i in range(Number_21[-1]+1,Number_21[-1]+1+Count):
            Number_21.append(i)
        
    elif((len(Number_21) + Count) < 21 ):
        for i in range(Number_21[-1]+1,Number_21[-1]+1+Count):
            Number_21.append(i)
        
    

    print("Its Computer Turn \n")
    print("Numbers Computer Going To Add :",Count)
    print("Computer : ",Number_21)

def Player_Turn():
    global Number_21,Game

    if(len(Number_21) != 0 and Number_21[-1] == 20):
        print("\nComputer Won the Game")
        Game = False
        return

    while True:
        try :
            print("Its Player Turn \n")
            Count = int(input("How Many Numbers You Are Going To Enter (1-5) : "))
            
            if(Count >= 1 and Count <= 5):
                if(len(Number_21) == 0):
                    for i in range(1,Count+1):
                        Number_21.append(i)
            
                elif((Number_21[-1] + Count) >= 21):
                    
                    print("\nComputer Won the Game")
                    Game = False
                    return
                else:
                    for i in range(Number_21[-1]+1,Number_21[-1]+1+Count):
                        Number_21.append(i)            
                break
            else:
                print("Only Between 1 - 5\n")
                    
        except:
            print("Invalid number")

    print("Player : ",Number_21)


print('''
⭐ Welcome To 21 Number Game ⭐
    
How To Play❓
    1. The game starts with the number 0.
    2. Players take turns to add 1, 2, or 3 to the current number.
    3. The player who reaches exactly 21 wins the game.
    4. If a player causes the number to exceed 21, they lose.

Let's Start⭐👍   
''')
Number_21 = []
 
Computer = 1
Game = True

while True:
    try:
        Player = int(input("Choose to start first or second (1/2): "))

        if(Player == 1 or Player == 2):
            if(Player == 1):
                Computer = 2
            break
        else:
            print("\nOnly 1 and 2 Position\n")
    except:
        print("\nInvalid Input\n")

Turn = 1

while(len(Number_21) < 21 and Game == True):
    # print(Turn)
    if(Turn == Player):
        Player_Turn()
    elif(Turn == Computer):
        Computer_Turn()
    if(Turn == 2):
        Turn = 1
    else : 
        Turn += 1