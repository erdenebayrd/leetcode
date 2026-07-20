class DSU:
    def __init__(self) -> None:
        self.parent = {}
        self.rank = {}
    
    def find_parent(self, node: int) -> int:
        if node not in self.parent:
            self.parent[node] = node
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union(self, node_u: int, node_v: int) -> None:
        parent_u = self.find_parent(node_u)
        parent_v = self.find_parent(node_v)
        if parent_u == parent_v:
            return
        if parent_v not in self.rank:
            self.rank[parent_v] = 1
        if parent_u not in self.rank:
            self.rank[parent_u] = 1
        if self.rank[parent_u] < self.rank[parent_v]:
            self.parent[parent_u] = self.parent[parent_v]
        elif self.rank[parent_u] > self.rank[parent_v]:
            self.parent[parent_v] = self.parent[parent_u]
        else: # self.rank[parent_u] == self.rank[parent_v]
            self.parent[parent_u] = self.parent[parent_v]
            self.rank[parent_v] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # time: O(N) N is total number of emails
        # space: O(N)
        # method: Union Find
        email_to_node = {}
        n = len(accounts)
        for i in range(n):
            for email in accounts[i][1:]:
                email_to_node[email] = i
        
        dsu = DSU()
        for i in range(n):
            for email in accounts[i][1:]:
                node_v = email_to_node[email]
                node_u = i
                dsu.union(node_v, node_u)
        
        merged_emails = {}
        for i in range(n):
            parent = dsu.find_parent(i)
            if parent not in merged_emails:
                merged_emails[parent] = []
            merged_emails[parent].extend(accounts[i][1:])
        
        result = []
        for parent_node_index in merged_emails:
            emails = sorted(set(merged_emails[parent_node_index]))
            name = accounts[parent_node_index][0]
            current = [name]
            current.extend(emails)
            result.append(current)
        return result