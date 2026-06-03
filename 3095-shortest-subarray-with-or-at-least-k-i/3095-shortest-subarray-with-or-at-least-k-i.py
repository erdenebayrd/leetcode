from collections import defaultdict

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # time: O(N log max(nums))
        # space: O(log(max(nums)))
        # method: sliding window + count
        n = len(nums)
        left = 0
        count = defaultdict(int)

        def add(number: int, ref: defaultdict) -> None:
            significant_bit = number.bit_length() - 1
            for i in range(significant_bit, -1, -1):
                if (1 << i) & number:
                    ref[i] += 1    
        
        def remove(number: int, ref: defaultdict) -> None:
            significant_bit = number.bit_length() - 1
            for i in range(significant_bit, -1, -1):
                if (1 << i) & number:
                    ref[i] -= 1
                    if ref[i] == 0:
                        del ref[i]

        def is_greater(ref: defaultdict, k: int) -> bool:
            number = 0
            for bit in ref:
                number |= (1 << bit)
            return number >= k
        
        result = float("inf")
        
        for right in range(n):
            number = nums[right]
            add(number, count)
            while left <= right and is_greater(count, k):
                result = min(result, right - left + 1)
                number = nums[left]
                remove(number, count)
                left += 1
        if result == float("inf"):
            result = -1
        return result
            