class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # time: O(n)
        # space: O(26)
        # method: monotonic stack
        visited = 0
        stack = []
        count = [0] * 26
        for ch in s:
            index = ord(ch) - ord('a')
            count[index] += 1

        for ch in s:
            index = ord(ch) - ord('a')
            count[index] -= 1
            if (1 << index) & visited:
                continue
            while stack and stack[-1] > index and count[stack[-1]] > 0:
                visited  ^= (1 << stack[-1]) # unvisited
                stack.pop()
            
            stack.append(index)
            visited |= (1 << index)
        return "".join([chr(i + ord('a')) for i in stack])