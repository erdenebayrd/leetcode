class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # time: O(N)
        # space: O(26)
        cnt = defaultdict(int)
        for ch in s:
            cnt[ch] += 1
        odd = 0
        for key in cnt:
            odd += cnt[key] & 1
        return odd <= 1