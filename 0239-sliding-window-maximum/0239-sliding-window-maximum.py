from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        obviously we can just check window of every movement to right but it till take O(N * K) time complexity which is not good
        first the important observation here is
            * if the number placed on a left is lower than one of number on it's right in a window, we don't need that number anymore
                [1 , -2, 3]  k =3
                in this case first 1 is useless because in a window there is a 3 which is greater than 1 we actually don't need 1 in here, -2 as well don't need
            * what we can do here is something like monotonic queue (strictly decreasing queue)
                [3, 2, 1]  k = 3
                the reason why it's decreasing is we are going to right direction (not left) and we are about to get a maximum value from each window
            
        what if there is a duplicated values
            * [_4_,  4, _1_,  3,  1] k = 5
            monotonic queue would be [4, 3, 1]
        when we move right by one we can store indices of actual numbers in monotonic queue
            * we can calculate the left most index in monotonic queue is in a window
        
            * the left most value of that index in monotonic queue would be the max value of each window
        """
        # time: O(N)
        # space: O(N)
        # method: monotinic queue stack
        n = len(nums)
        queue = deque() # indices
        for i in range(k - 1):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
        
        result = []
        for i in range(k - 1, n):
            
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            
            queue.append(i)

            while queue and queue[0] < i - k + 1:
                queue.popleft()

            result.append(nums[queue[0]])
            
        return result