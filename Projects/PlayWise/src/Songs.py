import json

class Songs:
    def __init__(self):
        with open("src/Songs.json","r") as D:
            Data = json.load(D)
        self.SongsDetails = Data[0]
        self.SongsData = Data[1]
        self.ID = self.SongsData[-1]["id"]
        self.LongestSong = self.SongsDetails[0]["LongestSong"]
        self.LongestSongData = self.SongsDetails[0]["LongestSongData"]
        self.RecentlyPlayed = self.SongsDetails[0]["RecentlyPlayed"]
    
    def SearchSong(self,id=None):
        if(id is None):
            Title = input("Title : ").strip()
            for D in self.SongsData:
                if(D["title"] == Title):
                    return D
            else:
                return self.SongsData[-1]
        elif(id is not None):
            for D in self.SongsData:
                if(D["id"] == id):
                    return D
        
    
    def Addsong(self,Tile,Artist,Duration):
        self.ID += 1
        
        Data = {"id": self.ID,
                "title": Tile,
                "artist": Artist,
                "duration": Duration}
        
        Song = self.SearchSong(self.LongestSong[0])
        print(Song)
        if(Duration > Song["duration"]):
            self.LongestSong.pop(-1)
            self.LongestSongData.pop(-1)
            
            self.LongestSong.insert(0,self.ID)
            self.LongestSongData.insert(0,Data)
            
        
        self.SongsDetails[0]["LongestSong"] = self.LongestSong
        self.SongsDetails[0]["LongestSongData"] = self.LongestSongData
        
        
        self.SongsData.append(Data)
        
        with open("src/Songs.json","w") as file:
            json.dump([self.SongsDetails,self.SongsData],file,indent=3)
    
    def export_snapshot(self):
        print("Top 5 Longest Songs")
        for i in range(5):
            print("\t",i+1,". ",self.LongestSongData[i]["title"])
        print()
        
        print("Most Recenty Played Songs")
        print()
        
        print("Song Count By Rating")
        print()
        
        
        
        
    
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
    
    # print(S1.Addsong("Adiyeh Kirukki","Vicanes Jay",450))
    
    S1.export_snapshot()
    
    print(S1.SearchSong())
    


        
        
    

