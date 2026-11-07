import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # time: O((n + m)* log (m)) n is number of tasks, m is number of servers
        # space: O(m)
        # method: min heap
        m = len(servers)
        free_servers = [(servers[i], i) for i in range(m)]
        heapq.heapify(free_servers)
        running_servers = []
        current_time = 0
        n = len(tasks)
        result = []
        for i in range(n):
            current_time = max(current_time, i)
            if not free_servers:
                seconds, _ = running_servers[0]
                current_time = max(current_time, seconds)
            
            while running_servers and running_servers[0][0] <= current_time:
                _, server_id = heapq.heappop(running_servers)
                heapq.heappush(free_servers, (servers[server_id], server_id))
            
            _, server_id = heapq.heappop(free_servers)
            result.append(server_id)
            process_time = tasks[i]
            heapq.heappush(running_servers, (current_time + process_time, server_id))
        
        return result