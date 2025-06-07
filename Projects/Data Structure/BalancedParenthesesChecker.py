def BalancedParenthesesChecker(Input):
    Stack = []
    Data = {')':'(',']':'[','}':'{'}
    for i in Input:
        if(i in Data.values()):
            Stack.append(i)
        elif(i in Data):
            if(len(Stack) > 0 and Data[i] == Stack[-1]):
                Stack.pop(-1)
            else:
                return False
    return(len(Stack)==0)

if(__name__ == "__main__"):
    print(BalancedParenthesesChecker("ASFV()"))
