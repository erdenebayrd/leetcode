class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        # time: O(N)
        # space: O(N)
        # method: reroot technique

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append((v, 0)) # no cost
            adj[v].append((u, 1)) # cost = 1
        
        def calculate_cost(node: int, parent: int) -> int:
            total = 0
            for neighbor, weight in adj[node]:
                if neighbor == parent:
                    continue
                total += calculate_cost(neighbor, node) + weight
            return total

        cost = [0] * n
        cost[0] = calculate_cost(0, -1)
        
        def reroot(node: int, parent: int) -> None:
            for neighbor, weight in adj[node]:
                if neighbor == parent:
                    continue
                if weight == 1: # node <--- neighbor
                    cost[neighbor] = cost[node] - 1
                else: # node ---> neighbor
                    cost[neighbor] = cost[node] + 1
                reroot(neighbor, node)
        
        reroot(0, -1)
        return cost
