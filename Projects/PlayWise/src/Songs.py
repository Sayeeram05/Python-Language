import json
from colorama import init, Fore, Back, Style

class Songs:
    def __init__(self):
        init(autoreset=True)
        with open("src/Songs.json","r") as D:
            Data = json.load(D)
        self.SongsDetails = Data[0]
        self.SongsData = Data[1]
        self.ID = self.SongsData[-1]["id"]
        self.LongestSongData = self.SongsDetails["LongestSongData"]
        self.RecentlyPlayed = self.SongsDetails["RecentlyPlayed"]
    
    def SearchSong(self,id=None):
        if(id is None):
            Title = input("Title : ").strip()
            for D in self.SongsData:
                if(D["title"].lower() == Title.lower()):
                    return D
            else:
                print(f"\n\nTitle : {Title} => Not Found")
                print("\n\n")
                return False
        elif(id is not None):
            for D in self.SongsData:
                if(D["id"] == id):
                    return D
        
    
    def Addsong(self,Title,Artist,Duration):
        self.ID += 1
        
        Data = {"id": self.ID,
                "title": Title,
                "artist": Artist,
                "duration": Duration}
        
        # print(Song)
        if(Duration > self.LongestSongData[0]["duration"]):
            self.LongestSongData.pop(-1)
            
            self.LongestSongData.insert(0,Data)
        elif(Duration > self.LongestSongData[-1]["duration"]):
            for i in range(1,5):
                if(self.LongestSongData[i]["duration"] < Duration):
                    self.LongestSongData.pop(-1)
                    
                    self.LongestSongData.insert(i-1,Data)
                    
                    break
            
        self.SongsDetails["LongestSongData"] = self.LongestSongData
        
        self.SongsData.append(Data)
        
        with open("src/Songs.json","w") as file:
            json.dump([self.SongsDetails,self.SongsData],file,indent=3)
    
    def export_snapshot(self):  
        with open("src/Songs.json","r") as D:
            Data = json.load(D)
        self.SongsDetails = Data[0]
        self.SongsData = Data[1]
        
        self.LongestSongData = self.SongsDetails["LongestSongData"]
        self.RecentlyPlayed = self.SongsDetails["RecentlyPlayed"]
        
          
        print("="*140)
        print(Style.BRIGHT + Fore.WHITE + Back.BLUE + "WELCOME TO PLAYWISE".center(140," "))
        print("="*140)
        
        longest_songs = [song["title"] for song in self.LongestSongData]
        recent_songs = [song["title"] for song in self.RecentlyPlayed]
        ratings = ["5 stars: 10", "4 stars: 7", "3 stars: 5", "2 stars: 2", "1 star: 1"]

        rows = max(len(longest_songs), len(recent_songs), len(ratings))
        longest_songs += [""] * (rows - len(longest_songs))
        recent_songs += [""] * (rows - len(recent_songs))
        ratings += [""] * (rows - len(ratings))

        total_width = 120
        column_width = (total_width) // 2  


        print(f"{'Top 5 Longest Songs':<{column_width}}{'Most Recently Played Songs':<{column_width}}{'Song Count By Rating':<{column_width}}")

        for i in range(rows):
            print("    ",end="")
            print(f"{longest_songs[i]:<{column_width}}{recent_songs[i]:<{column_width}}{ratings[i]:<{column_width}}")


        
        
        
        
    
if(__name__ == "__main__"):
    S1 = Songs()

    # Temp = []
    # for i in S1.SongsData:
    #     Temp.append([i["id"],i["duration"]])
    # Temp.sort()

    # Max = []
    # for i,j in Temp:
    #     if(len(Max) == 0):
    #         Max.append([i,j])
    #     elif(len(Max) <= 5):
    #         if(j > Max[0][-1]):
    #             Max.insert(0,[i,j])
    #     else:
    #         if(j > Max[0][-1]):
    #             Max.pop(-1)
    #             Max.insert(0,[i,j])
    # print(Max)
    
    # print(S1.ID,S1.LongestSong,S1.RecentlyPlayed)
    
    print(S1.Addsong("Adiyeh Kirukki","Vicanes Jay",290))
    
    S1.export_snapshot()
    
    
    

        
        
    

