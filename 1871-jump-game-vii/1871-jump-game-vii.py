from queue import Queue

class Solution:
    def canReach(self, s: str, min_jump: int, max_jump: int) -> bool:
        # time: O(N) N is length of string s
        # space: O(N)
        # method: bfs   
        queue = Queue()
        queue.put(0)
        n = len(s)
        left = right = -1

        while not queue.empty():
            index = queue.get()
            left = max(right + 1, index + min_jump)
            right = max(right, index + max_jump)
            for i in range(left, min(n, right + 1)):
                if s[i] == '1':
                    continue
                if n - 1 == i:
                    return True
                queue.put(i)
        return False