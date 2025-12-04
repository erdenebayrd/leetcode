class Solution:
    def countCollisions(self, directions: str) -> int:
        curR = 0
        leftCh = ""
        res = 0
        for d in directions:
            if d == "L":
                if curR > 0:
                    res += curR + 1
                    curR = 0
                    leftCh = "S"
                else: # curR == 0
                    if leftCh == "S":
                        res += 1
            elif d == "S":
                leftCh = "S"
                res += curR
                curR = 0
            else: # d == "R"
                curR += 1

        return res