class Solution {
public:
    int countElements(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int res = 0;
        for (int i = 0; i < nums.size(); i++) {
            int idx = prev(upper_bound(nums.begin(), nums.end(), nums[i])) - nums.begin();
            res += nums.size() - 1 - idx >= k;
        }
        return res;
    }
};