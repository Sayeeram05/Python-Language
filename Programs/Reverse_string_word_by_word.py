Sentence = input("Enter a Sentence: ")
Sentence = Sentence.split(" ")
for i in range(len(Sentence)):
    Sentence[i] = Sentence[i][-1::-1]
    
Output = " ".join(Sentence)
print("Reversed : ",Output)

Sentence.reverse()
print(Sentence)