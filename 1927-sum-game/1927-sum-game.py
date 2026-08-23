class Solution:
    def sumGame(self, num: str) -> bool:
        # time: O(N)
        # space: O(1)
        # method: math
        total = 0
        count = 0
        n = len(num)
        for i in range(n):
            if num[i] == '?':
                count += (1 if i < n // 2 else -1)
            else:
                total += (1 if i < n // 2 else -1) * int(num[i])
        
        alice = bob = count // 2
        if bob * 9 == -total and alice + (abs(count & 1)) == bob:
            return False
        return True