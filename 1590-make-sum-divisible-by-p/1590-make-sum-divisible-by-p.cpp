class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        int n = nums.size();
        int remainder = 0;
        for (int i = 0; i < n; i++) {
            remainder = (remainder + nums[i]) % p;
            if (i > 0) nums[i] += nums[i - 1];
            nums[i] %= p;
        }
        if (remainder == 0) return 0;
        int res = n;
        unordered_map<int, int> pos;
        for (int i = 0; i < n; i++) {
            if (nums[i] == remainder) res = min(res, i + 1);
            // (nums[i] - x) % p == remainder
            // nums[i] % p - x % p == remainder
            // (nums[i] - remainder + p) % p
            int x = (nums[i] - remainder + p) % p;
            if (pos[x] > 0) res = min(res, i - pos[x] + 1);
            pos[nums[i]] = i + 1;
        }
        if (res == n) res = -1;
        return res;
    }
};