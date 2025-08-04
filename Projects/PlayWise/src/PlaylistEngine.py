class Node:
    def __init__(self,ID,Title,Artist,Duration):
        self.Prev = None
        self.ID,self.Title,self.Artist,self.Duration = ID,Title,Artist,Duration
        self.Next = None
        
class PlaylistEngine:
    def __init__(self):
        self.Head = self.Tail = None
        self.Length = 0
    
    def isempty(self):
        return self.Head is None
    
    def Traversal(self):
        if(self.isempty()):
            print("\t No Songs")
        else:
            Temp = self.Head
            SNo = 1
            while(Temp != None):
                print(f"\t{SNo}. Title:{Temp.Title}   Artist:{Temp.Artist}  Duration:{Temp.Duration}")
                Temp = Temp.Next
                SNo += 1
        print("\n\n")
        # print("\nB : ",end="")
        # Temp = self.Tail
        # while(Temp != None):
        #     print(Temp.ID,Temp.Title,Temp.Artist,Temp.Duration,end=" ")
        #     Temp = Temp.Prev
        
         
    def add_song(self,ID,Title,Artist,Duration):
        NewNode = Node(ID,Title,Artist,Duration)
        if self.isempty():
            self.Head = self.Tail = NewNode
        else:
            self.Tail.Next = NewNode
            NewNode.Prev = self.Tail
            self.Tail = NewNode
        self.Length += 1
        
    def delete_song(self,index):
        if self.isempty() or index >= self.Length or index < 0:
            print(f"\n\nIndex : {index+1} => Invalid Index")
            return False
        
        elif(self.Head == self.Tail):
            Temp = self.Head
            self.Head = self.Tail = None
            
        elif(index == 0):
            Temp = self.Head
            self.Head = self.Head.Next
            self.Head.Prev = None
            
        elif(index == self.Length - 1):
            Temp = self.Tail
            self.Tail = self.Tail.Prev
            self.Tail.Next = None
            
        else:
            if(index < self.Length // 2):
                Temp = self.Head
                for _ in range(index):
                    Temp = Temp.Next
            else:
                Temp = self.Tail
                index = self.Length - 1 - index
                for _ in range(index):
                    Temp = Temp.Prev

            Temp.Prev.Next = Temp.Next
            Temp.Next.Prev = Temp.Prev
                
        self.Length -= 1
        Temp.Next = Temp.Prev = None
        return Temp
            
    def move_song(self,from_index,to_index):
        if(from_index == to_index or self.isempty() or from_index < 0 or from_index >= self.Length or to_index < 0 or to_index >= self.Length):
            print(f"Move Song : {from_index} To {to_index}   => Invalid Index")
        else:
            FromNode = self.delete_song(from_index)
            if(to_index == 0):
                self.Head.Prev = FromNode
                FromNode.Next = self.Head
                self.Head = FromNode
            elif(to_index == self.Length):
                self.Tail.Next = FromNode
                FromNode.Prev = self.Tail
                self.Tail = FromNode
            else:
                if(to_index < self.Length // 2):
                    # print("H")
                    Temp = self.Head
                    for _ in range(to_index):
                        Temp = Temp.Next
                else:
                    # print("T")
                    Temp = self.Tail
                    for _ in range(self.Length - 1 - to_index):
                        Temp = Temp.Prev
                # print(Temp.ID,Temp.Title,Temp.Artist,Temp.Duration,Temp.Prev,Temp.ID,Temp.Title,Temp.Artist,Temp.Duration)
                Temp.Prev.Next = FromNode
                FromNode.Next = Temp
                FromNode.Prev = Temp.Prev
                Temp.Prev = FromNode
                
            self.Length += 1 
            print(f"Move Song : {from_index} To {to_index}   => Sucessfully Moved") 
                         
    def reverse_playlist(self):
        if self.isempty():
            return -1
        else:
            Temp = self.Head
            while(Temp is not None):
                NextNode = Temp.Next
                Temp.Prev,Temp.Next = Temp.Next,Temp.Prev
                Temp = NextNode
            self.Head,self.Tail = self.Tail,self.Head
    

if __name__ == "__main__":
    P1 = PlaylistEngine()
    P1.add_song(1)
    P1.add_song(2)
    P1.add_song(3)
    P1.add_song(4)
    P1.add_song(5)
    
    P1.Traversal()
    
    # P1.delete_song(0)
    # P1.Traversal()
    
    # P1.delete_song(3)
    # P1.Traversal()
    
    # P1.delete_song(2)
    # P1.Traversal()
    
    P1.move_song(4,0)
    P1.Traversal()
    