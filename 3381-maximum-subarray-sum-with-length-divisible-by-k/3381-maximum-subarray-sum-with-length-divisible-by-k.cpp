class Solution {
public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> prefix_sum(n, 0);
        prefix_sum[0] = nums[0];
        for (int i = 1; i < n; i++) prefix_sum[i] += prefix_sum[i - 1] + nums[i];
        function <long long(int, int)> range_sum = [&](int l, int r) {
            if (l == 0) return prefix_sum[r];
            return prefix_sum[r] - prefix_sum[l - 1];
        };
        const long long inf = (long long)(2e14);
        vector<long long> dp(n, -inf);
        dp[k - 1] = range_sum(0, k - 1);
        for (int i = k; i < n; i++) {
            long long k_sum = range_sum(i - k + 1, i);
            // cout << i - k + 1 << " " << i << " " << k_sum << endl;
            dp[i] = max(k_sum, k_sum + dp[i - k]);
        }
        // for (int i = 0; i < n; i++) cout << dp[i] << " "; cout << endl;
        return *max_element(dp.begin(), dp.end());
    }
};