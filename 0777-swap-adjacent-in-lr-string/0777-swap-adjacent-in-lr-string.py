class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if Counter(start) != Counter(result):
            return False
        n = len(start)
        start = list(start)
        result = list(result)
        startIndexL = 0
        startIndexX = 0

        def findNext(startIndex: int, ch: str, acceptable: str) -> int:
            nonlocal startIndexL, startIndexX
            if ch == "L":
                startIndex = max(startIndex + 1, startIndexL)
            if ch == "X":
                startIndex = max(startIndex + 1, startIndexX)

            for i in range(startIndex, n):
                if ch == "L":
                    startIndexL = i
                if ch == "X":
                    startIndexX = i
                if ch == start[i]:
                    return i
                elif start[i] != acceptable:
                    return -1
            return -1

        for i in range(n):
            if start[i] == result[i]:
                continue
            elif start[i] == 'X' and result[i] == 'R':
                return False
            elif start[i] == 'X' and result[i] == 'L':
                index = findNext(i, 'L', 'X')
                if index == -1:
                    return False
                # swap
                start[i], start[index] = start[index], start[i]
            elif start[i] == 'L' and result[i] == 'X':
                return False
            elif start[i] == 'L' and result[i] == 'R':
                return False
            elif start[i] == 'R' and result[i] == 'X':
                index = findNext(i, 'X', 'R')
                if index == -1:
                    return False
                # swap
                start[i], start[index] = start[index], start[i]
            elif start[i] == 'R' and result[i] == 'L':
                return False
            else:
                assert False
        return True