class Solution:
    def checkString(self, s: str) -> bool:
        b = False
        for ch in s:
            if ch == 'b':
                b = True
            
            if b and ch == 'a':
                return False
        return True