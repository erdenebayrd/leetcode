from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # time: O(26 * N)
        # space: O(N)
        # method: DFS

        count = Counter(s)
        n = len(target)

        def dfs(index: int) -> int:
            if index == n:
                for ch in count:
                    if count[ch] > 0:
                        return n
                return -1
            
            result = -1
            ch = target[index]
            if ch in count and count[ch] > 0:
                count[ch] -= 1
                result = max(result, dfs(index + 1))
                count[ch] += 1
            
            for ch_s in count:
                if ch_s > ch and count[ch_s] > 0:
                    result = max(result, index)

            return result
        
        index = dfs(0)
        if index == -1:
            return ""
        
        result = []
        for i in range(index):
            count[target[i]] -= 1
            result.append(target[i])
        
        char = ""
        for ch in count:
            if ch > target[index] and count[ch] > 0:
                if char == "" or char > ch:
                    char = ch
        
        count[char] -= 1
        result.append(char)
        curr = []
        for ch in count:
            curr.extend([ch] * count[ch])
        curr.sort()
        result.extend(curr)
        return "".join(result)
            