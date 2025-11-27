class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int N = int(1e4);
        int cnt[int(2e4)];
        memset(cnt, 0, sizeof cnt);
        int n = nums.size();
        for (int i = 0; i < n; i++) cnt[nums[i] + N]++;
        vector<pair<int, int>> arr;
        for (int i = 0; i < n; i++) {
            if (cnt[nums[i] + N] == 0) continue;
            arr.push_back({cnt[nums[i] + N], nums[i]});
            cnt[nums[i] + N] = 0;
        }
        sort(arr.begin(), arr.end(), greater<pair<int, int>>());
        vector <int> res;
        for (int i = 0; i < k; i++) res.push_back(arr[i].second);
        return res;
    }
};