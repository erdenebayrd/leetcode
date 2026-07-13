# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        """
        observations
            * somehow if we serialize the given tree and sub_stree into flat text and pattern, it will become pattern search problem from string
            * we need to serialize a tree into text as O(length of tree)
            * after converting root into text and sub_root into pattern, we can use Z-Function algorithm to find pattern in text that will take O(N) time and space.
        """
        # time: O(N) N is number of nodes in root + number of nodes in sub_root
        # space: O(N)
        # method: serialize + pattern search

        # def serialize(node: Optional[TreeNode]) -> str:
        #     # we can use stack iterative way to serialize tree into string
        #     stack = [node]
        #     result = []
        #     while stack:
        #         node = stack.pop() # takes last node
        #         if node:
        #             result.append("^" + str(node.val))
        #             stack.append(node.right)
        #             stack.append(node.left)
        #         else: # node is None
        #             result.append("#")
        #     return ",".join(result)
        
        # text = serialize(root)
        # pattern = serialize(sub_root)

        # def find(text: str, pattern: str) -> bool:
        #     # in this case we will use z function which is O(length text + length pattern) time & space complexity
        #     text = pattern + text
        #     n = len(text)
        #     z_values = [0] * n
        #     z_values[0] = n

        #     left = right = 0
        #     for i in range(1, n):
        #         if i <= right: # "i" is inside [left, right] range, meaning, starting from 0 -> (right - left) == [left, right], then we can use calculated z_value
        #             z_values[i] = min(z_values[i - left], right - i + 1)
                
        #         while i + z_values[i] < n and text[z_values[i]] == text[i + z_values[i]]:
        #             z_values[i] += 1
                
        #         if i + z_values[i] - 1 > right:
        #             left = i
        #             right = i + z_values[i] - 1

        #     for i in range(1, n):
        #         if z_values[i] >= len(pattern):
        #             return True
        #     return False

        # is_sub_tree = find(text, pattern)
        # return is_sub_tree


        # # ------------------ Merkle Tree O(n + m) ---------------------
        # # time: O(n + m)
        # # space: O(n + m)
        # # method: merkle tree using hash builtin function

        # if not root or not sub_root:
        #     return False
        
        # def get_hash(node: Optional[TreeNode]) -> int:
        #     if not node:
        #         return 0
            
        #     left_hash = get_hash(node.left)
        #     right_hash = get_hash(node.right)
        #     node_hash = hash(node.val)
        #     hash_value = hash((node_hash, left_hash, right_hash))
        #     return hash_value
        
        # sub_tree_hash = get_hash(sub_root)
        
        # def find(node: Optional[TreeNode], sub_tree_hash: int) -> tuple: # first value is hash value of subtree at node, second value is found a subtree_hash value (bool)
        #     if not node:
        #         return (0, False)
        #     left_hash, is_found_left = find(node.left, sub_tree_hash)
        #     right_hash, is_found_right = find(node.right, sub_tree_hash)
        #     node_hash = hash(node.val)
        #     hash_value = hash((node_hash, left_hash, right_hash))
        #     is_found = (hash_value == sub_tree_hash) or is_found_left or is_found_right
        #     return (hash_value, is_found)

        # _, is_found = find(root, sub_tree_hash)
        # return is_found

        # __________________________________ ISOMORPHISM __________________________________
        # time: O(N + M)
        # space: O(N)
        # method: isomorphic tree -> like a merkle tree
        
        def get_id(node: Optional[TreeNode], ref_ids: dict) -> int:
            if not node:
                return -1
            left_id = get_id(node.left, ref_ids)
            right_id = get_id(node.right, ref_ids)
            current = (node.val, left_id, right_id)
            if current not in ref_ids:
                ref_ids[current] = len(ref_ids)
            return ref_ids[current]

        ref_ids = {}
        root_id = get_id(root, ref_ids)
        sub_root_id = get_id(sub_root, ref_ids)

        return sub_root_id <= root_id
        