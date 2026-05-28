class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # time: O(N)
        # space: O(N)
        # method: hashmap
        n = len(s)
        mapping = {}
        reversed_mapping = {}
        for i in range(n):
            if s[i] not in mapping:
                mapping[s[i]] = t[i]
            if t[i] not in reversed_mapping:
                reversed_mapping[t[i]] = s[i]
            if mapping[s[i]] != t[i] or reversed_mapping[t[i]] != s[i]:
                return False
        return True