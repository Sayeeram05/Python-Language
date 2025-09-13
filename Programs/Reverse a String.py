def Reverse(word):
    L = len(word)
    if(L == 1):
        return word[0]
    else:
        return word[-1] + Reverse(word[:L-1])
    
print(Reverse("Hello"))
