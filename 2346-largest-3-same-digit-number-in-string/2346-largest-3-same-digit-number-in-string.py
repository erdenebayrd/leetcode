class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        mx = -1
        for i in range(len(num) - 2):
            s = num[i:i+3]
            if len(set(s)) == 1:
               if mx < int(s):
                mx = int(s)
                res = s
        return res 
