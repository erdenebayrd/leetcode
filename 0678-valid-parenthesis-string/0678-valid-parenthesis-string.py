class Solution:
    def checkValidString(self, s: str) -> bool:
        # time: O(n) n is len of s
        # space: O(1)
        # method: Greedy

        count_open_interval = [0, 0]
        for ch in s:
            if ch == '(':
                count_open_interval[0] += 1
                count_open_interval[1] += 1
            elif ch == ')':
                count_open_interval[0] = max(0, count_open_interval[0] - 1)
                count_open_interval[1] -= 1
            else: # *
                count_open_interval[0] = max(0, count_open_interval[0] - 1)
                count_open_interval[1] += 1

            if count_open_interval[1] < 0:
                return False
        
        return count_open_interval[0] == 0



