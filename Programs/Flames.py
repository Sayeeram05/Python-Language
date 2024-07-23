print('''
⭐ Welcome to the FLAMES Game! ⭐

How to Play❓
1. Enter the names of two players.
2. Calculate the total number of unique characters in both names combined.
3. Use this number to count through the letters in FLAMES: 
   - F: Friends
   - L: Lovers
   - A: Affectionate
   - M: Married
   - E: Enemies
   - S: Siblings
4. Keep counting and removing letters in FLAMES until only one letter remains. This letter determines the relationship type.

Let's Start! ⭐👍
''')

BoyName = list(input("Boy Name : ").lower())
GirlName = list(input("Girl Name : ").lower())

Comman = 0

for i in BoyName:
    if(i in GirlName):
        Comman += 2  
    
Count = len(BoyName) + len(GirlName) - Comman

Flames = ['Friends','Lovers','Affectionate','Married','Enemies','Siblings']

Position = 0
while(len(Flames) > 1):
    Position += Count % len(Flames)

    if(Position == 0):
        Flames.pop(len(Flames)-1)
        Position = 0
    elif(Position > len(Flames)):
        Count = Position  
        Position = 0  # Aldready Positon is added
        continue
    else:
        Flames.pop(Position-1)
        Position -= 1  # Index 

    # print(Flames)
    Count = len(BoyName) + len(GirlName) - Comman

print("Relationship status : ",Flames[0])

