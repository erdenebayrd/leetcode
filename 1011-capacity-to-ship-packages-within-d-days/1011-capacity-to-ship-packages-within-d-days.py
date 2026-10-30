class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # time: O(n * log (sum(weights)))
        # space: O(1)
        # method: bin search

        def check(limit: int) -> bool:
            count = current = 0
            for weight in weights:
                if weight > limit:
                    return False
                if current + weight <= limit:
                    current += weight
                else:
                    current = weight
                    count += 1
            return count + 1 <= days

        low, high = 0, sum(weights) + 1
        while low + 1 < high:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid
        
        return high