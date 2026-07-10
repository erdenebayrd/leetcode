class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], max_diff: int, queries: List[List[int]]) -> List[int]:
        # time: O(N log N)
        # space: O(N log N)
        # method: sparse table + sort
        node = []
        for i in range(n):
            value = nums[i]
            node.append((value, i))
        node.sort()
        m = int(log2(n)) + 2
        st = [[-1] * m for _ in range(n)]
        for i in range(n):
            value_u, u = node[i]
            # valuej - value <= max_diff
            # valuej <= max_diff + value
            low, high = i - 1, n
            while low + 1 < high:
                mid = (low + high) // 2
                value_v, v = node[mid]
                if value_v - value_u <= max_diff:
                    low = mid
                else:
                    high = mid
            _, v = node[low]
            st[u][0] = v
        for level in range(1, m):
            for i in range(n):
                _, u = node[i]
                st[u][level] = st[st[u][level - 1]][level - 1]
        
        order = [-1] * n
        for i in range(n):
            _, u = node[i]
            order[u] = i
            
        answer = []
        for u, v in queries:
            if u == v:
                answer.append(0)
                continue
            
            if order[u] > order[v]:
                u, v = v, u

            if order[st[u][-1]] < order[v]:
                answer.append(-1)
                continue

            distance = 0
            for level in range(m - 1, -1, -1):
                if order[st[u][level]] < order[v]:
                    u = st[u][level]
                    distance += (1 << level)
            
            answer.append(distance + 1)
        return answer