import json

class Node:
    def __init__(self,ID,Title,Artist,Duration):
        self.ID,self.Title,self.Artist,self.Duration = ID,Title,Artist,Duration
        self.Next = None
        
class PlayBack:
    def __init__(self):
        self.Head = None
        
        with open("src/Songs.json", "r") as Data:
            RecentlyPlayedData = json.load(Data)
            
        RecentlyPlayedData = RecentlyPlayedData[0]["RecentlyPlayed"]

        if(RecentlyPlayedData):
            for Data in RecentlyPlayedData:
                self.Push(Data["id"],Data["title"],Data["artist"],Data["duration"])
            
    def isempty(self):
        return self.Head is None
    
    def Traversal(self):
        Temp = self.Head
        print("Recently Played Songs : ")
        i = 1
        while(Temp is not None):
            print(f"\t{i}. Title:{Temp.Title}   Artist:{Temp.Artist}  Duration:{Temp.Duration}")
            Temp = Temp.Next
            i += 1
        
    
    def Push(self,ID,Title,Artist,Duration):
        NewNode = Node(ID,Title,Artist,Duration)
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
            return Temp.ID,Temp.Title,Temp.Artist,Temp.Duration
        else:
            Temp = self.Head
            self.Head = self.Head.Next
            return Temp.ID,Temp.Title,Temp.Artist,Temp.Duration
        
if(__name__ == "__main__"):
    S1 = PlayBack()
    S1.Traversal()
    
