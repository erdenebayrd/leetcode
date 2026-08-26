from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # time: O(N)
        # space: O(N)
        # method: Onion Peeling to get centers

        adj = defaultdict(list)
        degree = defaultdict(int)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        centers = set([i for i in range(n)])
        leaves = []
        for i in range(n):
            if degree[i] == 1: # leaf node
                leaves.append(i)
        
        while len(centers) > 2:
            new_leaves = []
            for leaf in leaves:
                centers.remove(leaf)
                for neighbor in adj[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        new_leaves.append(neighbor)
            leaves = new_leaves
        return list(centers)