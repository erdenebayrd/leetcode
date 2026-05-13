import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        """
        lets think in this way

        there are 2 list of servers
            1. free servers
            2. running servers (task assigned servers)
        initially all server weights in a free servers

        we can iterate through the tasks one by one

        at the i 'th task
        we can assign this task into one of the free servers with lowest weight
        but before we assign
        we have to check running servers
        if current time stamp is greather or equal to the timestamp which the assigned task is done
        we should move that servers into free servers

        we can use minimum heap at free servers and runnig servers

        free servers min heap by weight and index
        running servers by timestamp (freed) and server index

        initially current time stamp is 0

        we assign task one by one and increase current time stamp
        """
        # time: O(N log N)
        # space: O(N)
        # method: 2 min heap

        free = [(servers[server_index], server_index) for server_index in range(len(servers))]
        running = []
        heapq.heapify(free)
    
        n = len(tasks)
        result = [-1] * n

        current_timestamp = 0

        for i in range(n):
            current_timestamp = max(current_timestamp, i)

            if not free:
                current_timestamp = running[0][0]

            while running and current_timestamp >= running[0][0]:
                freed_timestamp, server_index = heapq.heappop(running)
                heapq.heappush(free, (servers[server_index], server_index))
            
            _, server_index = heapq.heappop(free)
            result[i] = server_index
            heapq.heappush(running, (tasks[i] + current_timestamp, server_index))

        return result