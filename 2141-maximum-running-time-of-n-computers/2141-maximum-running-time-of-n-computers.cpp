class Solution {
public:
    long long maxRunTime(int n, vector<int>& batteries) {
        long long lo = *min_element(batteries.begin(), batteries.end()) - 1;
        long long hi = accumulate(batteries.begin(), batteries.end(), 0LL) + 1;
        while (lo + 1LL < hi) {
            long long md = (lo + hi) / 2LL;
            long long total = 0;
            for (auto x: batteries) total += min(md, (long long)x);
            if (md * (long long)n <= total) lo = md;
            else hi = md;
        }
        return lo;
    }
};