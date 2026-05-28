# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        
                 3                3
                /                  \
               5                    5

               this tree example is not considered as duplicated

               * same structure
               * same values

               we can use AHU algo giving uniq id to every subtree based their value and structure
               for null node we give -1 id
               for example

                   4
                 /   \
              NULL   NULL

              the shape of subtree rooted at 4 would be tuple (4, -1, -1)
              and if this shape is found in a dictionary (tree_ids) we would return already calculated id
              if not, we just give this shape to the next id then store it on the dictionary

              (4, -1, -1) id become 0

                            7
                          /. \  
                        /       \
                      /           \
                   4               3
                 /   \           /.  \
              NULL   NULL     NULL    NULL

              (4, -1, -1) id become 0
              (3, -1, -1) id become 1
              (7, 0, 1) id = 2

            so the time complexity would become O(N) N is the number of vertices in the tree
            space O(N) due to storing all ids
        """
        # time: O(N) N is the number of vertices in the tree
        # space: O(N)
        # method: AHU algo (isomorphic, merkle tree)

        if not root:
            return []
        
        def get_id(node: Optional[TreeNode], tree_ids: dict, node_ids: dict) -> int:
            if not node:
                return -1
            left_id = get_id(node.left, tree_ids, node_ids)
            right_id = get_id(node.right, tree_ids, node_ids)
            subtree_shape = (node.val, left_id, right_id)
            if subtree_shape not in tree_ids:
                tree_ids[subtree_shape] = len(tree_ids)
            node_ids[node] = tree_ids[subtree_shape]
            return tree_ids[subtree_shape]
        
        node_ids = {}
        tree_ids = {} # key as shape of subtree rooted at every node, value as given unique id for every unique shapes

        get_id(root, tree_ids, node_ids)

        count_id = defaultdict(int)
        result = []
        for node in node_ids:
            subtree_id = node_ids[node]
            count_id[subtree_id] += 1
            if count_id[subtree_id] == 2:
                result.append(node)
        return result