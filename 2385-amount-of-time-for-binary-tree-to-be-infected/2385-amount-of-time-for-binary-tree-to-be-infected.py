from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjacentList = defaultdict(list)

        def dfs(currentNode: Optional[TreeNode]) -> None:
            if currentNode.left is not None:
                adjacentList[currentNode.val].append(currentNode.left.val)
                adjacentList[currentNode.left.val].append(currentNode.val)
                dfs(currentNode.left)
            if currentNode.right is not None:
                adjacentList[currentNode.val].append(currentNode.right.val)
                adjacentList[currentNode.right.val].append(currentNode.val)
                dfs(currentNode.right)
        
        dfs(root)
        queue = deque()
        cost = 0
        queue.append([start, cost])
        visited = set()
        visited.add(start)
        
        result = 0
        while queue:
            currentNode, currentCost = queue.popleft()
            result = max(currentCost, result)
            for neighbor in adjacentList[currentNode]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append([neighbor, currentCost + 1])
        return result