class Node:
    def __init__(self,Data):
        self.Prev = None
        self.Data = Data
        self.Next = None
    
class PlaylistEngine:
    def __init__(self):
        self.Head = self.Tail = None
        self.Length = 0
    
    def isempty(self):
        return self.Head is None
    
    def Traversal(self):
        print("F : ",end="")
        Temp = self.Head
        while(Temp != None):
            print(Temp.Data,end=" ")
            Temp = Temp.Next
        
        print("\nB : ",end="")
        Temp = self.Tail
        while(Temp != None):
            print(Temp.Data,end=" ")
            Temp = Temp.Prev
        print()
        
        
    def add_song(self,Data):
        self.Length += 1
        NewNode = Node(Data)
        if self.isempty():
            self.Head = self.Tail = NewNode
        else:
            self.Tail.Next = NewNode
            NewNode.Prev = self.Tail
            self.Tail = NewNode
        
        self.Traversal()

    def delete_song(self,index):
        if self.isempty() or index >= self.Length:
            return False
        elif(self.Length - index < index):
            pass
        else:
            pass
             
    def move_song(self,from_index,to_index):
        pass
    
    def reverse_playlist(self):
        pass

if __name__ == "__main__":
    P1 = PlaylistEngine()
    P1.add_song(1)
    P1.add_song(2)
    P1.add_song(3)
    