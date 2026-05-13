from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        # time: O(N log N)
        # space: O(N)
        # method: binary search + frequency

        n = len(s)
        target = n // 4

        search_pattern = {"Q": 0, "W": 0, "E": 0, "R": 0}
        count = Counter(s)
        total = 0
        for character in count:
            if count[character] > target:
                search_pattern[character] = count[character] - target
                total += count[character] - target
        if total == 0:
            return 0

        def check(length: int) -> bool:
            current_count = Counter()
            for i in range(length):
                current_count[s[i]] += 1
            for i in range(length, n):
                flag = True
                for character in search_pattern:
                    flag &= current_count[character] >= search_pattern[character]
                if flag:
                    return True
                current_count[s[i]] += 1
                current_count[s[i - length]] -= 1
            flag = True
            for character in search_pattern:
                flag &= current_count[character] >= search_pattern[character]
            return flag

        low, high = total - 1, n + 1
        while low + 1 < high:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid
        return high
        