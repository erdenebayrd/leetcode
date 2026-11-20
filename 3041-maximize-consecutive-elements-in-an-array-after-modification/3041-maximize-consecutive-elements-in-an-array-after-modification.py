class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        # time: O(n log n)
        # space: O(n)
        # method: DP + sortin
        count = Counter(nums)
        arr = []
        for number in count:
            for _ in range(min(2, count[number])):
                arr.append(number)
        
        n = len(arr)
        left = sorted(arr)
        right = left[:]
        for i in range(n):
            right[i] += 1
        
        left = left + [0, -1]
        right = right + [0, -1]

        # print(left)
        # print(right)

        @cache
        def solve(index: int, is_left: bool) -> int:
            if is_left:
                value = left[index]
            else:
                value = right[index]

            count = 0
            if value + 1 == left[index + 1]:
                count = max(count, solve(index + 1, True))
            if value + 1 == right[index + 1]:
                count = max(count, solve(index + 1, False))
            
            if not is_left and value == right[index + 1]:
                if value + 1 == left[index + 2]:
                    count = max(count, solve(index + 2, True))
                if value + 1 == right[index + 2]:
                    count = max(count, solve(index + 2, False))
                    
            count += 1 # adding itself
            
            return count
        
        result = 0
        for i in range(n):
            result = max(result, solve(i, True))
            result = max(result, solve(i, False))
        
        return result