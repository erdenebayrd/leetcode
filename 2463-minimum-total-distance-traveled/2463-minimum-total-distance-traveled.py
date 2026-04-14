from typing import List
from collections import deque

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort both robots and factories by position
        robot.sort()
        factory.sort()
        
        m = len(robot)
        # dp[j] represents the min cost to assign the first j robots.
        # Initially, 0 robots cost 0. Everything else is infinity.
        dp = [float('inf')] * (m + 1)
        dp[0] = 0
        
        for f_pos, limit in factory:
            next_dp = [float('inf')] * (m + 1)
            next_dp[0] = 0
            
            # Deque stores tuples: (u, value)
            # value = dp[u] - prefix[u]
            q = deque()
            
            # Base case for the queue: u = 0
            q.append((0, dp[0] - 0)) 
            
            prefix = 0
            
            for j in range(1, m + 1):
                # Update the prefix sum of distances for the current robot
                prefix += abs(robot[j - 1] - f_pos)
                
                # 1. Pop elements from the left that are outside our "limit" sliding window
                while q and q[0][0] < j - limit:
                    q.popleft()
                
                # 2. Prepare the current `u = j` value to insert into the monotonic queue
                # We want to maintain a monotonically increasing queue of values to easily find the min
                val = dp[j] - prefix
                while q and q[-1][1] >= val:
                    q.pop()
                q.append((j, val))
                
                # 3. The minimum value for our window is always at the front of the deque
                next_dp[j] = q[0][1] + prefix
            
            # Move to the next factory
            dp = next_dp
            
        return dp[m]