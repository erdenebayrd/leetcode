class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for o in operations:
            if "--" in o:
                res -= 1
                continue
            res += 1
        return res