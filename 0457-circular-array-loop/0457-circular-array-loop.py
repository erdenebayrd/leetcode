class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # # time: O(N)
        # # space: O(N)
        # # method: Kahn's cycle detection algo
        # n = len(nums)

        # def hasCycle(edges) -> bool: # O(V + E)
        #     adj = defaultdict(list)
        #     indegree = defaultdict(int)
        #     nodes = set()
        #     for fromNode, toNode in edges:
        #         adj[fromNode].append(toNode)
        #         indegree[toNode] += 1
        #         nodes.add(fromNode)
        #         nodes.add(toNode)
            
        #     queue = deque()
        #     for node in nodes:
        #         if indegree[node] == 0:
        #             queue.append(node)
            
        #     while queue:
        #         node = queue.popleft()
        #         for neighbor in adj[node]:
        #             indegree[neighbor] -= 1
        #             if indegree[neighbor] == 0:
        #                 queue.append(neighbor)
        #     for node in nodes:
        #         if indegree[node] > 0:
        #             return True
        #     return False

        # edges = []
        # # we take only positivies
        # for node in range(n):
        #     # (node) -> (node + nums[node]) % n
        #     if nums[node] < 0:
        #         continue
        #     nextNode = (node + nums[node]) % n
        #     if node == nextNode:
        #         continue
        #     edges.append([node, nextNode])
        
        # if hasCycle(edges):
        #     return True
        
        # edges = []
        # # we take only negatives
        # for node in range(n):
        #     if nums[node] > 0:
        #         continue
        #     nextNode = (node + nums[node]) % n
        #     if node == nextNode:
        #         continue
        #     edges.append([node, nextNode])
        
        # return hasCycle(edges)

        # ------------------------------------------- Floyd's cycle finding algo -------------------------------------------
        # time: O(N)
        # space: O(1)
        # method: Floyd's cycle finding algo
        
        n = len(nums)

        def forward(node: int) -> Optional[int]:
            if nums[node] < 0:
                return None
            nextNode = (node + nums[node]) % n
            if nextNode == node:
                return None
            return nextNode
        
        def backward(node: int) -> Optional[int]:
            if nums[node] > 0:
                return None
            nextNode = (node + nums[node]) % n
            if nextNode == node:
                return None
            return nextNode
        
        def hasCycle(node: int) -> bool:
            result = False
            # forward
            slow = node
            fast = node
            while fast is not None and forward(fast) is not None:
                slow = forward(slow)
                fast = forward(forward(fast))
                if slow == fast:
                    result |= True
                    break

            # backward
            slow = node
            fast = node
            while fast is not None and backward(fast) is not None:
                slow = backward(slow)
                fast = backward(backward(fast))
                if slow == fast:
                    result |= True
                    break
            
            # marking visited nodes
            currentNode = node
            while currentNode is not None:
                nextNode = forward(currentNode)
                nums[currentNode] = 0
                currentNode = nextNode

            currentNode = node
            while currentNode is not None:
                prevNode = backward(currentNode)
                nums[currentNode] = 0
                currentNode = prevNode

            return result
        
        for i in range(n):
            if hasCycle(i) is True:
                return True
        return False