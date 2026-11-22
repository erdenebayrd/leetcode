class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        # time: O(n)
        # space: O(n)
        # method: DFS

        n = len(s)

        def get_adj(parents: list):
            adj = defaultdict(list)
            for i in range(1, len(parents)):
                adj[parents[i]].append(i)    
            return adj

        parents = parent[:]
        seen = defaultdict(list)
        adj = get_adj(parent)

        def dfs(node: int):

            if seen[s[node]]:
                parents[node] = seen[s[node]][-1]

            seen[s[node]].append(node)
            for ch in adj[node]:
                dfs(ch)
            
            seen[s[node]].pop()

        dfs(0)

        adj = get_adj(parents)
        answer = [0] * len(s)

        def count(node: int) -> int:
            result = 1
            for ch in adj[node]:
                result += count(ch)
            answer[node] = result
            return result
        
        count(0)

        return answer
