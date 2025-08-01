class Node:
    def __init__(self,Data):
        self.Data = Data
        self.Next = None
        
class Playback:
    def __init__(self):
        self.Head = None
        
    def isempty(self):
        return self.Head is None
    
    def Traversal(self):
        Temp = self.Head
        print("Stack : ",end="")
        while(Temp is not None):
            print(Temp.Data,end=" ")
            Temp = Temp.Next
        print()
    
    def Push(self,Data):
        NewNode = Node(Data)
        if(self.isempty()):
            self.Head = NewNode
        else:
            NewNode.Next = self.Head
            self.Head = NewNode
            
    def Pop(self):
        if(self.isempty()):
            return False
        elif(self.Head.Next == None):
            Temp = self.Head
            self.Head = None
            return Temp.Data
        else:
            Temp = self.Head
            self.Head = self.Head.Next
            return Temp.Data
        
if(__name__ == "__main__"):
    S1 = Playback()
    for i in range(1,10):
        S1.Push(i)
    S1.Traversal()
    
    for i in range(1,10):
        S1.Pop()
    
    S1.Traversal()
