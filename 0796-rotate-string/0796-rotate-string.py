class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        s = "abcde", goal = "cdeab"
        abcdeabcde
          cdeab
        """
        if len(s) != len(goal):
            return False

        text = goal + s + s
        n = len(text)
        left, right = -1, -1
        z = [0] * n
        length = 0
        for i in range(1, n):

            if i <= right:
                prev_i = i - left
                prev_length = z[prev_i]
                length = min(prev_length, right - i + 1)

            while i + length < n and text[length] == text[i + length]:
                length += 1

            z[i] = length
            if i + length - 1 >= right:
                right = i + length - 1
                left = i
        # # """
        # # ['a', 'b', 'c', 'd', '#', 'b', 'c', 'a', 'd', 'b', 'c', 'a', 'd']
        # # [ 0,   0,   0,   0,   0,   0,   0,   1,   3,   4,   4,   4,   4 ]
        # # """
        # print(list(text))
        # print(z)

        return max(z) >= len(goal)
        