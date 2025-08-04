import os
import time
from Songs import Songs
from Library import Library as Lib
from colorama import init, Fore, Back, Style

class Home:
    def __init__(self):
        os.system("cls")
        init(autoreset=True)
        
        self.Songs = Songs()
        self.Library = Lib()
        
        self.HomePage()
    
        
    def ModifyPlaylist(self,name=None):
        if(name is None):
            name = input("\nName : ")
        if(name in self.Library.LibrarList):
            while True:
                print(f"PlayList : {name}")
                print("\t1. Add Song")
                print("\t2. Delete Song")
                print("\t3. View Songs")
                print("\t4. Move Song")
                print("\t5. Go To Home")
                
                option = input("\nEnter : ").strip()
                if(option == "1"):
                    Data = self.Songs.SearchSong()
                    # print(Data)
                    if(Data):
                        self.Library.LibrarList[name].add_song(Data["id"],Data["title"],Data["artist"],Data["duration"])
                        print(f"\n\nTitle : {Data["title"]} => Added in {name}")
                        print("\n\n")
                elif(option == "2"):
                    Position = int(input("Position : "))
                    Data = self.Library.LibrarList[name].delete_song(Position-1)
                    # print(Data)
                    if(Data):
                        print(f"\n\nTitle : {Data.Title} => Deleted in {name}")
                        print("\n\n")
                elif(option == "3"):
                    print(f"Playlist : {name}")
                    self.Library.LibrarList[name].Traversal()
                elif(option == "4"):
                    From = int(input("From : "))
                    To = int(input("To : "))
                    self.Library.LibrarList[name].move_song(From,To)
                elif(option == "5"):
                    print("\n\n Moving To HomePage\n\n")
                    time.sleep(1)
                    os.system("cls")
                    break
                else:
                    print("\n\nInvalid Selection\n\n")
                time.sleep(2)
                os.system("cls")
        else:
            print(f"\n\nPlaylist : {name} => Invalid\n\n")
            time.sleep(2)
            os.system("cls")
            
    
    def HomePage(self):
        while(True):
            self.Songs.export_snapshot()
            print("\n")
            print("Select : ")
            print("\t1. Create Playlist")
            print("\t2. View All Playlist")
            print("\t3. Delete Playlist")
            print("\t4. Modify Playlist")
            print("\t5. Play Playlist")
            print("\t6. Exit")
            
            Option = int(input("\nOption : "))
            
            if(Option == 1):
                print("\nCreate Playlist")
                name = input("\nName : ")
                self.Library.AddPlaylist(name)
                self.ModifyPlaylist(name)
            elif(Option == 2):
                print("\n\View Playlist")
                self.Library.ViewLibrary()
                
            elif(Option == 3):
                print("\n\Delete Playlist")
                name = input("\nName : ")
                self.Library.DeletePlaylist(name)
                
            elif(Option == 4):
                print("\n\Modify Playlist")
                name = input("\nName : ")
                self.ModifyPlaylist(name)

            elif(Option == 5):
                print("\nPlay Playlist")
                name = input("\nName : ")
                self.Library.PlayPlaylist(name)
                
            elif(Option == 6):
                os.system("cls")
                
                print("="*140)
                print(Style.BRIGHT + Fore.WHITE + Back.BLUE + "Let's Meet Again".center(140," "))
                print("="*140)

                time.sleep(2)
                break
                
                
            else:
                pass     
            

Home()
    
    