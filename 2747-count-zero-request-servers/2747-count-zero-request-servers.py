class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # time: O(N * log N + Q * log Q)
        # space: O(N + Q)
        # method: sorting
        sorted_logs = sorted(logs, key=lambda x: x[1])
        sorted_queries = sorted([(q_time, i) for i, q_time in enumerate(queries)])
        left = right = -1
        count_availables = [0] * len(queries)
        used_servers = {}
        for query_time, index in sorted_queries:
            while right + 1 < len(sorted_logs) and sorted_logs[right + 1][1] <= query_time:
                server_id = sorted_logs[right + 1][0]
                if server_id not in used_servers:
                    used_servers[server_id] = 0
                used_servers[server_id] += 1
                right += 1
            
            while left + 1 < len(sorted_logs) and sorted_logs[left + 1][1] < query_time - x:
                server_id = sorted_logs[left + 1][0]
                used_servers[server_id] -= 1
                if used_servers[server_id] == 0:
                    del used_servers[server_id]
                left += 1
            count_availables[index] = n - len(used_servers)
        return count_availables