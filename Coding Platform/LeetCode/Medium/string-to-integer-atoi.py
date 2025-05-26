class Solution:
    def myAtoi(self, s: str) -> int:
        n = ""
        for i in s:
            if(i == " " and n == ""):
                continue
            elif(i.isdigit()):
                n += i
            elif((i == "+" or i == "-") and n == "" and ("+" not in i or "-" not in i)):
                n += i
            else:
                break
        if(n == "" or n == "+" or n == "-"):
            return 0
        else:
            check = 2147483648
            print(n)
            n = int(n)
            if(n > check-1):
                return check-1
            elif(n < -check):
                return -check
            else:
                return n