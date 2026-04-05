class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # time: O(N)
        # space: O(N)
        # method: monotonic stack
        result = []
        queue = deque() # monotonic stack queue
        n = len(nums)
        
        def add(number: int) -> None:
            while queue and queue[-1] > number:
                queue.pop()
            queue.append(number)

        index = 0
        while k > 0:
            while index < n - k + 1:
                add(nums[index])
                index += 1
            result.append(queue[0])
            queue.popleft()
            k -= 1
        return result