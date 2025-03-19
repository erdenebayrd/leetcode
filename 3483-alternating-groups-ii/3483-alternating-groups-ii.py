class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # O(N) time complexity
        # O(1) space complexity
        cur, res, n = 0, 0, len(colors)
        for i in range(1, k):
            cur += colors[i] ^ colors[i - 1]
        for i in range(n):
            if cur == k - 1:
                res += 1
            cur -= colors[i] ^ colors[(i + 1) % n]
            cur += colors[(i + k) % n] ^ colors[(i + k - 1) % n]
        return res