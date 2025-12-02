/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool twoSumBSTs(TreeNode* root1, TreeNode* root2, int target) {
        function <bool(int, TreeNode*)> search = [&](int val, TreeNode* cur) {
            if (cur == NULL) return false;
            if (cur -> val == val) return true;
            if (cur -> val > val) cur = cur -> left;
            else cur = cur -> right;
            return search(val, cur);
        };
        function <bool(TreeNode*)> dfs = [&](TreeNode* cur) {
            if (cur == NULL) return false;
            bool res = search(target - (cur -> val), root2);
            res |= dfs(cur -> left);
            res |= dfs(cur -> right);
            return res;
        };
        return dfs(root1);
    }
};