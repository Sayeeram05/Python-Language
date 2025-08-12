from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        Five = 0
        Ten = 0
        for i in bills:
            if(i == 5):
                Five += 1
            elif(i == 10):
                if(Five > 0):
                    Five -= 1
                    Ten += 1
                else:
                    return False
            else:
                if(Ten >= 1 and Five >= 1):
                    Ten -= 1
                    Five -= 1
                elif(Five >= 3):
                    Five -= 3
                else:
                    return False
        return True