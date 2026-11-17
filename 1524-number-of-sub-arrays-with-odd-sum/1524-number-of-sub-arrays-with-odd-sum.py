class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: xor
        n = len(arr)
        result = 0
        current = 0
        count_zero = 1
        count_one = 0
        mod = int(1e9 + 7)
        for i in range(n):
            current ^= (arr[i] & 1)
            if current:
                result += count_zero
                count_one += 1
            else:
                result += count_one
                count_zero += 1
        return result % mod