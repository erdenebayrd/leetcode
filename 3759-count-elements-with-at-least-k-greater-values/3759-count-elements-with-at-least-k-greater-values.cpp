class Solution {
public:
    int countElements(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        unordered_map<int, int> pos;
        for (int i = 0; i < n; i++) pos[nums[i]] = i;
        int res = 0;
        for (int i = 0; i < n; i++) {
            int cnt = n - pos[nums[i]] - 1;
            if (cnt >= k) res += 1;
        }
        return res;
    }
};