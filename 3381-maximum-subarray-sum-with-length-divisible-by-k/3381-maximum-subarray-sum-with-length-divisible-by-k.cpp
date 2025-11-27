class Solution {
private:
    vector<long long> prefixSum;
    long long rangeSum(int l, int r) {
        if (l == 0) return prefixSum[r];
        return prefixSum[r] - prefixSum[l - 1];
    }

public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        prefixSum.assign(n, 0);
        prefixSum[0] = nums[0];
        for (int i = 1; i < n; i++) prefixSum[i] += prefixSum[i - 1] + nums[i];
        const long long inf = (long long)(2e14);
        vector<long long> dp(n, -inf);
        dp[k - 1] = rangeSum(0, k - 1);
        for (int i = k; i < n; i++) {
            long long kSum = rangeSum(i - k + 1, i);
            // cout << i - k + 1 << " " << i << " " << kSum << endl;
            dp[i] = max(kSum, kSum + dp[i - k]);
        }
        // for (int i = 0; i < n; i++) cout << dp[i] << " "; cout << endl;
        return *max_element(dp.begin(), dp.end());
    }
};