class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        const int N = int(1e4);
        int cnt[int(2e4) + 1];
        memset(cnt, 0, sizeof cnt);
        vector<int> rev[n + 1];
        for (int i = 0; i < n; i++) cnt[nums[i] + N] += 1;
        vector<int> freq(n + 1, 0);
        for (int i = 0; i <= int(2e4); i++) {
            if (cnt[i] == 0) continue;
            rev[cnt[i]].push_back(i - N);
            freq[cnt[i]] += 1;
        }
        vector<int> res;
        for (int i = n; k > 0 && i > 0; i--) {
            int idx = 0;
            while (k > 0 && freq[i] > 0) {
                freq[i]--; k--;
                res.push_back(rev[i][idx++]);
            }
        }
        return res;
    }
};