class Node:
    def __init__(self,rate):
        self.rate = rate
        self.Songs = []
        self.Left = self.Right = None 
        
class Rating:
    def __init__(self):
        self.root = None
    
    def InsertSong(self,id,rate):
        def Insert(node,rate):
            if(node is None):
                NewNode = Node(rate)
                NewNode.Songs.append(id)
                return NewNode
            elif(rate < node.rate):
                node.Left = Insert(node.Left,rate)
            elif(rate > node.rate):
                node.Right = Insert(node.Right,rate)
            else:
                node.Songs.append(id)
            return node
        self.root = Insert(self.root,rate)
        
    

R1 = Rating()
R1.InsertSong(100,1)
R1.InsertSong(150,1)
R1.InsertSong(100,2)
R1.InsertSong(150,2)
R1.InsertSong(170,3)
R1.InsertSong(180,4)
R1.InsertSong(200,5)

Temp = R1.root
while(Temp is not None):
    print(Temp.Left,Temp.rate,Temp.Songs,Temp.Right)
    Temp = Temp.Right
            
            