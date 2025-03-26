class Solution:
    def canChange(self, start: str, target: str) -> bool:
        arrStart = []
        for i, ch in enumerate(start):
            if ch != "_":
                arrStart.append((ch, i))
        arrTarget = []
        for i, ch in enumerate(target):
            if ch != "_":
                arrTarget.append((ch, i))
        if len(arrTarget) != len(arrStart):
            return False
        for i in range(len(arrTarget)):
            if arrStart[i][0] != arrTarget[i][0]:
                return False
            if arrStart[i][0] == "L" and arrStart[i][1] < arrTarget[i][1]:
                return False
            if arrStart[i][0] == "R" and arrStart[i][1] > arrTarget[i][1]:
                return False
        return True