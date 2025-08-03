from PlaylistEngine import PlaylistEngine

class Library(PlaylistEngine):
    def __init__(self):
        self.LibrarList = dict()
    
    def ViewLibrary(self):
        print("Library : ",end="")
        if(len(self.LibrarList) == 0):
            print("Empty")
        else:
            print()
            for Name in self.LibrarList:
                print("\t1.",Name)
            print()
        
    def AddPlaylist(self,Name):
        if(Name in self.LibrarList):
            return False
        else:
            PlayList = PlaylistEngine()
            self.LibrarList[Name] = PlayList
            
    def DeletePlaylist(self,Name):
        if(Name not in self.LibrarList):
            return False
        else:
            self.LibrarList.pop(Name)
    
    