from collections import deque 

class Solution:
    def canReach(self, s: str, min_jump: int, max_jump: int) -> bool:
        """
        first observation is the last index is 0 or 1. if it's 1, no chance to reach there
        second thing is
            * we need to never visit each index more than once
            * but also don't need to check every index is visited or not, it will take time
            * to do that we can take care of latest index we reached, lets call it "right"
            * for example we are at the index "i" we can jump into [i + min_jump -> i + max_jump]
                if "right" index is greater than i + min_jump, we don't need to check [i + min_jump -> right] since we already know we reached nodes (indices) between them
            * initially "right" is 0 since we are already at index 0
        
        so we can do in bfs so that time and space complexity would be O(N) N is length of string s
        """
        # time: O(N)
        # space: O(N)
        # method: BFS + sliding window ( right most node )
        if s[-1] == '1':
            return False
        
        n = len(s)
        queue = deque()
        queue.append(0)
        right = 0
        while queue:
            node = queue.popleft()
            if node == n - 1:
                return True
            start = max(right + 1, node + min_jump)
            end = min(n - 1, node + max_jump)
            for neighbor in range(start, end + 1):
                if s[neighbor] == '0':
                    queue.append(neighbor)
            right = max(right, node + max_jump)

        return False