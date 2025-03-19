class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        if ones <= 1 or ones == len(data):
            return 0
        curOnes = sum(data[:ones])
        res = ones - curOnes
        for i in range(ones, len(data)):
            if data[i - ones] == 1:
                curOnes -= 1
            if data[i] == 1:
                curOnes += 1
            res = min(res, ones - curOnes)
        return res