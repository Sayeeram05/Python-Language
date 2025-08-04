import json
import time
from PlaylistEngine import PlaylistEngine
import os
from colorama import init, Back, Style
from PlayBack import PlayBack


class Library(PlaylistEngine):
    def __init__(self):
        self.LibrarList = dict()
        init(autoreset=True)
        self.PlayBack = PlayBack()
    
    def ViewLibrary(self):
        print("\n\nLibrary : ",end="")
        if(len(self.LibrarList) == 0):
            print("Empty\n\n")
        else:
            print()
            index = 1
            for Name in self.LibrarList:
                print(f"\t{index}.",Name)
                index += 1
            print("\n\n")
        time.sleep(2)
        os.system("cls")
        
    def AddPlaylist(self,Name):
        if(Name in self.LibrarList):
            print(f"\n\nPlaylist : {Name} => Aldready in Library")
            print("\n\n")
        else:
            PlayList = PlaylistEngine()
            self.LibrarList[Name] = PlayList
            print(f"\n\nSucessfully Playlist : {Name} Added in Library")
            print("\n\n")
        time.sleep(2)
        os.system("cls")
            
            
    def DeletePlaylist(self,Name):
        if(Name not in self.LibrarList):
            print(f"\n\nPlaylist : {Name} => Not Found in Library")
            print("\n\n")
        else:
            self.LibrarList.pop(Name)
            print(f"\n\nSucessfully Playlist : {Name} Deleted From Library")
            print("\n\n")
        time.sleep(2)
        os.system("cls")
    
    def PlayPlaylist(self,Name):
        if(Name not in self.LibrarList):
            print(f"\n\nPlaylist : {Name} => Not Found in Library")
            print("\n\n")
            time.sleep(2)
            os.system("cls")
        else:
            Temp = self.LibrarList[Name].Head
            # print(Temp)
            if(Temp is None):
                print(f"\n\nPlaylist : {Name} => Empty")
                print("\n\n")
                time.sleep(2)
                os.system("cls")
            else:
                while(Temp is not None):
                    for i in range(1,101):
                        print(f"PlayList : {Name}")
                        print(f"\tSong Details =>  Title:{Temp.Title}   Artist:{Temp.Artist}  Duration:{Temp.Duration}\n")
                        print("="*100)
                        print(Style.BRIGHT + Back.BLUE + " "*i)
                        print("="*100)
                        time.sleep(0.05)
                        if(i < 100):
                            os.system("cls")
                            
                    self.PlayBack.Push(Temp.ID,Temp.Title,Temp.Artist,Temp.Duration)
                            
                    print(f"\n\nPlayList : {Name}")
                    print("\nOptions : ")
                    print("\t1. Next Song")
                    print("\t2. Previous Song")
                    print("\t3. PlayBack Song")
                    print("\t4. Exit")
                    
                    Option = int(input("\nOption : "))
                    if(Option == 1):
                        if(Temp.Next is None):
                            print(f"\n\nPlayList {Name} : Played\n\n")
                            break
                        else:
                            Temp = Temp.Next
                            print("\n\n Playing Next Song\n\n")
                            
                    elif(Option == 2):
                        if(Temp.Prev is None):
                            print(f"\n\nSong : {Temp.Title} => First Song")
                        else:
                            Temp = Temp.Prev
                            print("\n\n Playing Previous Song\n\n")
                            
                    elif(Option == 3):
                        self.LibrarList[Name].add_song(Temp.ID,Temp.Title,Temp.Artist,Temp.Duration)
                        if(Temp.Next is None):
                            print(f"\n\nPlayList {Name} : Played\n\n")
                            break
                        else:
                            print(f"\n\nPlayList {Name} : Added in Playlist {Name}\n\n")
                            self.LibrarList[Name].Traversal()
                            
                            Temp = Temp.Next
                            print("\n\n Playing Next Song\n\n")
                        
                        
                    elif(Option == 4):
                        with open("src/Songs.json" , "r") as D:
                            Data = json.load(D)
                        
                        SongDeatails = Data[0]
                        SongsData = Data[1]
                        
                        SongDeatails["RecentlyPlayed"].clear()
                        
                        Temp = self.PlayBack.Head
                        for _ in range(5):
                            if(Temp is None):
                                break
                            SongDeatails["RecentlyPlayed"].append({
                                "id": Temp.ID,
                                "title": Temp.Title,
                                "artist": Temp.Artist,
                                "duration": Temp.Duration
                              })
                            Temp = Temp.Next
                        
                        with open("src/Songs.json" , "w") as D:
                            json.dump([SongDeatails,SongsData],D,indent=3)
                        
                        print("\n\nMoving Back To Home\n\n")
                        time.sleep(1)
                        os.system("cls")
                        break
                        
                    else:
                        print("\n\nInvalid Option\n\n")
                    
                    time.sleep(1)
                    os.system("cls")
                    
                    
                    
                    
                    
        
def Test():
    for i in range(1,101):
        print("="*100)
        print(Style.BRIGHT + Back.BLUE + " "*i)
        print("="*100)
        time.sleep(0.05)
        if(i < 100):
            os.system("cls")
            
if(__name__ == "__main__"):
    init(autoreset=True)
    Test()