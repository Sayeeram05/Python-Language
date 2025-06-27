def WordCount(Input):
    Dict = {}
    Input = Input.split(" ")
    while(len(Input) > 0):
        if Input[0] in Dict:
            Dict[Input[0]] += 1
        else:
            Dict[Input[0]] = 1
        Input.pop(0)    

    return Dict
    
print(WordCount("apple banana apple apple mango"))