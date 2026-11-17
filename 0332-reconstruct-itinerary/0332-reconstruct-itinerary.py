class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for source, target in sorted(tickets, reverse=True):
            if source not in adj:
                adj[source] = []
            adj[source].append(target)
        
        path = []
        def dfs(node: str) -> None:
            if node not in adj or not adj[node]:
                return

            while adj[node]:
                neighbor = adj[node][-1]
                adj[node].pop()
                dfs(neighbor)
                path.append(neighbor)
        
        dfs("JFK")
        path.append("JFK")
        return path[::-1]