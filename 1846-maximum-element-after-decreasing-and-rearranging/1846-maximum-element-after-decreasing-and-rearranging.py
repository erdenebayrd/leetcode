class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        cur = 1
        for element in arr:
            if cur <= element:
                cur += 1
        return cur - 1