import random
class RandomizedSet:

    def __init__(self):
        self.Data = []
    
    def insert(self, val: int) -> bool:
        if(val in self.Data):
            return False
        else:
            self.Data.append(val)
            self
            return True
    def remove(self, val: int) -> bool:
        if(val in self.Data):
            self.Data.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        Temp = random.choice(self.Data)
        return Temp
