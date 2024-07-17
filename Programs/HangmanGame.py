import random   

WordList = fruits = ["Apple","Banana","Orange","Grape","Strawberry","Pineapple","Watermelon","Mango","Kiwi","Pear","Cherry","Blueberry","Peach","Plum","Raspberry","Lemon","Lime","Coconut","Pomegranate","Apricot"]

RandomFruit = random.choice(WordList).lower()  # Randomly stores the word in lower case

GameLetters = []    # Empty list to "display" the "RandomFruit" in _ _ _ _ _ (underlines)

def CreateGameLetters():    # Function to "add" the "_" to the "GameLetters" respect to the "length" of "RandomFruit"
    for i in range(0,len(RandomFruit)):
        GameLetters.append("_")  # add the _ at last

def Setup():
    print('''\n\n--> Let's Play Hangman Game !!! <--  
    \nHow To Play?
    \t1.Find All The Letters Of The Fruit
    \t2.At Last Program Will Show The Number Of Attempts\n''')

    print("Word List = ",end="")
    print(*WordList,sep=", ")   # Shows the list to user

    print("\n------- Lets Start 👍 -------")

if(__name__ == "__main__"):     # Runs Only in this File (print(__name__))
    Setup()
    CreateGameLetters()

    length = 0  # To Break the Wile Loop

    while length < len(RandomFruit):
        print("\nGuess The Letters :  ",end="")
        print(*GameLetters,sep=" ")

        try : 
            GussedLetter = input("\nEnter The Gussed Letter : ").lower()
        except Exception as e:
            print(e,": Enter Alphabet Letter")
        finally:
            flag = 0    # To check the GuessedLetter is in RandomFruit
            for i in range(0,len(RandomFruit)):
                if(RandomFruit[i] == GussedLetter and GameLetters[i] == "_"):
                    GameLetters[i] = GussedLetter
                    flag = 1
                    length = length + 1
                    break

            print(("\nWrong Guess ❌" if(flag == 0) else ("\nAwesome 👌\n")))
            
    print("\nGood Job 👍")

else:
    print("Run The Program In Hangmag File")
