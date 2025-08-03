from Library import Library as Lib
from Songs import Songs as Sng

class Main:
    def __init__(self):
        self.Library = Lib()
        self.Songs = Sng()
    
    def OpenPlaylist(self):
        name = input("Name : ")
        if(name in self.Library.LibrarList):
            while True:
                print("""
                    Select : 
                        1. Add Song
                        2. Delete Song
                        3. View Songs
                        4. Move Song
                        5. Play Song
                        
                    """)
                option = input("Enter : ").strip()
                if(option == "1"):
                    Data = self.Songs.get()
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
                else:
                    break
        else:
            print(False)
    
    def Start(self):
        while True:
            print('''
                    Select :
                        1. View Library
                        2. Create Playlist
                        3. Delete Playlist
                        4. Open Playlist
                        5. Exit
                ''')
            option = input("Enter : ").strip()

            if option == "1":
                self.Library.ViewLibrary()

            elif option == "2":
                name = input("Name : ")
                self.Library.AddPlaylist(name)

            elif option == "3":
                name = input("Name : ")
                self.Library.DeletePlaylist(name)

            elif option == "4":
                self.OpenPlaylist()

            elif option == "5":
                print("Exiting program.")
                break

            else:
                print("Invalid option. Please choose 1 to 5.")
    
if __name__ == "__main__":
    User = Main()
    User.Start()
