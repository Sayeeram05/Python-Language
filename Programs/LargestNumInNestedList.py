print('''
Program To Find The Largest Number In A Nested List
    1.Iterate a Nested List
    2.Use Try And Expect to Iterate Nested List
    3.Find the Largest Number
''')
Value = 0

def RecursionFunction(Data):
    for i in Data:
        try:
            RecursionFunction(i)  # If i is an int Then It Throws an error for iterating int
        except:
            global Value
            if(i > Value):
                Value = i
            # print(i)
         
Data = [2,9,4,[1,3,4],[5,7,8,[21,4]],[8,9,10],3]

print("Nested List : ",Data)

RecursionFunction(Data)

print("Largest Number :",Value)



