from collections import defaultdict

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        """
            for every vertex as a center of the star graph
                * iterate all its neighbors
                * find max sum at most k edges (might be 0 edges if all neighbors values are negative)
            after all, maximum value of centers would be the answer
        """
        # time: O(V + E)
        # space: O(V + E)
        # method: graph

        adjacent_list = defaultdict(list)
        for u, v in edges:
            adjacent_list[u].append(v)
            adjacent_list[v].append(u)
        
        center_values = vals[:]
        for node in adjacent_list:
            neighbor_values = []
            for neighbor in adjacent_list[node]:
                neighbor_values.append(vals[neighbor])
            neighbor_values.sort(reverse=True)
            neighbor_values = neighbor_values[:k]
            total_neighbor_value = 0
            for value in neighbor_values:
                if value > 0:
                    total_neighbor_value += value
            center_values[node] += total_neighbor_value
        return max(center_values)