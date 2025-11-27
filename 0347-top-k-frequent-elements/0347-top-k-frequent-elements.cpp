class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, int> ump;
        unordered_map<int, vector<int>> rev;
        for (int i = 0; i < n; i++) ump[nums[i]] += 1;
        vector<int> freq(n + 1, 0);
        for (auto x: ump) {
            rev[x.second].push_back(x.first);
            freq[x.second] += 1;
        }
        vector<int> res;
        // count sort O(N)
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