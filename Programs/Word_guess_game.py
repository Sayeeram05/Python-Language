import random

print('''
⭐ Welcome To Word Gussing Game ⭐
    
How To Play❓
    1.Computer Randomly choose a number a Word from a list 
    2.Player have to guess the alphabet in the word
    3.Player will form the word from guessing one by one letter

Let's Start⭐👍   
''')
Words_List = ("artificial intelligence", "blockchain", "cloud computing", "cybersecurity", "data analytics", "internet of things", "machine learning", "quantum computing", "virtual reality")


comp_word = random.choice(Words_List) # Random word 

print("Word list :",Words_List,"\n")

guessed_word = []
print(comp_word)

for i in comp_word:
    if(i == " "):
        guessed_word.append(" ")
    else:
        guessed_word.append("_")

print("Computer Randomly selected a word from the list 👌\n\nNow it's Your turn 👍\n")
print("Guessed Word : ",end="")

for i in guessed_word:
    print(i,end="")
print("\n")

while("_" in guessed_word):  # Loop stops when uers guessed the word
    letter = input("Gussed Letter (1 letter): ")[0].lower()

    if(letter in comp_word): 
        print("Correct Guess 👍\n")
        index = int(comp_word.index(letter)) # finds the position of letter
        
        if(guessed_word[index] == letter): # checks wethear the user is aldready guessed the letter

            for i in range(index+1,len(comp_word)): # iterate the word for the next index
                if(comp_word[i] == letter and guessed_word[i] != letter): # finds the position of letter and also guessed word is empty
                    guessed_word[i] = letter
                    break # unwanted loops
                    
        else:
            guessed_word[index] = letter
        
        print("Guessed Word : ",end="")

        for i in guessed_word:
            print(i,end="")
        print("\n")

    else:
        print("Invalid Input or Worng Choice\n")

print("Thank you 👍")