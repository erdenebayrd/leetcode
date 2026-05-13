from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        # time: O(N)
        # space: O(1)
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

        current_count = Counter()
        left = 0
        count_found = 0
        for character in search_pattern:
            if search_pattern[character] == 0:
                count_found += 1
        
        result = n
        for right in range(n):
            current_count[s[right]] += 1
            if current_count[s[right]] == search_pattern[s[right]]:
                count_found += 1

            while left <= right and count_found == len(search_pattern):
                result = min(result, right - left + 1)
                current_count[s[left]] -= 1
                if current_count[s[left]] + 1 == search_pattern[s[left]]:
                    count_found -= 1
                left += 1
        return result