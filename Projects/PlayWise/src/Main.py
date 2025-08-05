import json
import os
import time
from Library import Library
from Songs import Songs
from PlayBack import PlayBack
from colorama import init, Fore, Back, Style
from Dashboard import Dashboard

class Main:
    def __init__(self):
        self.Songs = Songs()
        init(autoreset=True)
        self.PlayBack = PlayBack()
        self.Dashboard = Dashboard()
        self.Library = Library()
        
    def Exit(self):
        os.system("cls")
                
        print("="*140)
        print(Style.BRIGHT + Fore.WHITE + Back.BLUE + "Let's Meet Again".center(140," "))
        print("="*140)

        time.sleep(2)
        
        
    
    def Start(self):
        while(True):
            self.Songs.export_snapshot()
            print("\n\nDashBoard") 
            print("\t1. Library")
            print("\t2. Play Song")
            print("\t3. Rating")
            print("\t4. Songs")
            print("\t5. Exit")
            Option = input("\nSelected Option : ")
            
            time.sleep(1)
            os.system("cls")
            
            if(Option == "1"):
                self.Dashboard.LibraryPage()
            elif(Option == "2"):
                self.Library.PlayPlaylist()
            elif(Option == "3"):
                pass
            elif(Option == "4"):
                self.Songs.SongPage()
                pass
            elif(Option == "5"):
                self.Exit()
                break
            else:
                print("\n\nInvalid Option\n\n")
                
            time.sleep(2)
            os.system("cls")
        
        
        
        
        
if __name__ == "__main__":

    User = Main()
    
    User.Start()
    
