class Solution {
private:
    int reverse(int x) {
        int res = 0;
        while (x > 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        return res;
    }
public:
    int minMirrorPairDistance(vector<int>& nums) {
        unordered_map<int, vector<int>> pos;
        int n = nums.size();
        for (int i = 0; i < n; i++) pos[nums[i]].push_back(i);
        int res = n;
        for (int i = 0; i < n; i++) {
            int x = reverse(nums[i]);
            if (pos.find(x) == pos.end()) continue;
            auto it = upper_bound(pos[x].begin(), pos[x].end(), i);
            if (it == pos[x].end()) continue;
            res = min(*it - i, res);
        }
        if (res == n) res = -1;
        return res;
    }
};