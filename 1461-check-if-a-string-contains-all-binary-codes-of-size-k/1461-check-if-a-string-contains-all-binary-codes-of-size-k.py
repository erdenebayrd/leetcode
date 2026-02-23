class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        current = 0
        n = len(s)
        if n < (1 << k):
            return False
            
        for i in range(k):
            current = current * 2 + int(s[i])
        count = set()
        count.add(current)
        for i in range(k, n):
            current = current * 2 + int(s[i])
            kbit = current & (1 << k)
            current ^= kbit
            count.add(current)
        
        return len(count) == (1 << k)