import os
import time
from Songs import Songs
from Library import Library as Lib

class Home:
    def __init__(self):
        os.system("cls")
        
        self.Songs = Songs()
        self.Library = Lib()
        
        print("\033[1m\033[94m WELCOME TO PLAYWISE \033[0m".center(50," "))
        self.HomePage()
        print("\n")
    
    def ModifyPlaylist(self,name=None):
        if(name is None):
            name = input("Name : ")
        if(name in self.Library.LibrarList):
            while True:
                print("Select")
                print("\t1. Add Song")
                print("\t2. Delete Song")
                print("\t3. View Songs")
                print("\t4. Move Song")
                print("\t5. Play Song")
                print("\t6. Go To Home")
                
                option = input("Enter : ").strip()
                if(option == "1"):
                    Data = self.Songs.SearchSong()
                    print(Data)
                    self.Library.LibrarList[name].add_song(Data["id"],Data["title"],Data["artist"],Data["duration"])
                elif(option == "2"):
                    Position = int(input("Position : "))
                    self.Library.LibrarList[name].delete_song(Position-1)
                elif(option == "3"):
                    self.Library.LibrarList[name].Traversal()
                elif(option == "4"):
                    From = int(input("From : "))
                    To = int(input("To : "))
                    self.Library.LibrarList[name].move_song(From,To)
                elif(option == "5"):
                    pass
                else:
                    break
        else:
            print(False)
            
    
    def HomePage(self):
        self.Songs.export_snapshot()
        while(True):
            print("Select : ")
            print("\t1. Create Playlist")
            print("\t2. View Playlist")
            print("\t3. Delete Playlist")
            print("\t4. Modify Playlist")
            print("\t5. Play Playlist")
            print("\t6. Exit")
            
            Option = int(input("Option : "))
            
            if (Option == 1):
                name = input("Name : ")
                self.Library.AddPlaylist(name)
                self.ModifyPlaylist(name)
            elif (Option == 2):
                self.Library.ViewLibrary()
                
            elif (Option == 3):
                name = input("Name : ")
                self.Library.DeletePlaylist(name)
                
            elif (Option == 4):
                pass
            elif (Option == 5):
                break
            else:
                pass     

Home()
    
    