class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(N)
        # method: simulation & pointer hashmap

        n = len(nums)
        root = Node(nums[0] % 10)
        hashmap = {}
        hashmap[(1, 1)] = root
        for i in range(1, n):
            level = nums[i] // 100
            pos = (nums[i] // 10) % 10
            value = nums[i] % 10
            node = Node(value)
            hashmap[(level, pos)] = node

            parent_level = level - 1
            parent_pos = (pos + 1) // 2
            parent_node = hashmap[(parent_level, parent_pos)]

            if pos & 1: # left child
                parent_node.left = node
            else: # right child
                parent_node.right = node
            
        def dfs(cur: Node, cur_sum: int) -> int:
            cur_sum += cur.value
            if not cur.left and not cur.right:
                return cur_sum
            result = 0
            if cur.left:
                result += dfs(cur.left, cur_sum)
            if cur.right:
                result += dfs(cur.right, cur_sum)
            return result
        
        return dfs(root, 0)