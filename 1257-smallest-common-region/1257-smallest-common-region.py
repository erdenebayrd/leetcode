class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        # time: O(N)
        # space: O(N)
        # method: tree LCA

        tree_ids = {}
        def get_id(node: str) -> str:
            if node not in tree_ids:
                tree_ids[node] = len(tree_ids)
            return tree_ids[node]

        hashmap = {}
        parent = {}
        root_candidates = []
        adj = {}
        for region_list in regions:
            subroot = float("inf")
            for i, region in enumerate(region_list):
                node_id = get_id(region)
                hashmap[node_id] = region
                if node_id not in adj:
                    adj[node_id] = []
                if i == 0:
                    subroot = node_id
                    root_candidates.append(subroot)
                    continue
                parent[node_id] = subroot
                adj[subroot].append(node_id)
        
        root = float('inf')
        for root_candidate in root_candidates:
            if root_candidate not in parent:
                root = root_candidate
                break

        levels = {}
        def dfs(node_id: int, levels: dict, deep: int) -> None:
            levels[node_id] = deep
            for child_id in adj[node_id]:
                dfs(child_id, levels, deep + 1)
        
        dfs(root, levels, 0)
        region1_id = get_id(region1)
        region2_id = get_id(region2)

        while levels[region1_id] != levels[region2_id]:
            if levels[region1_id] > levels[region2_id]:
                region1_id = parent[region1_id]
            else:
                region2_id = parent[region2_id]
        
        while region1_id != region2_id:
            region1_id = parent[region1_id]
            region2_id = parent[region2_id]
        
        return hashmap[region1_id]