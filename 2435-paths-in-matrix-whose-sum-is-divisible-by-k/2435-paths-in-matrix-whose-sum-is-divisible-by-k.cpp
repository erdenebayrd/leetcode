class Solution {
public:
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        int mod = (int)(1e9) + 7;
        int n = grid.size();
        int m = grid[0].size();
        if (n == 1 && m == 1) {
            return grid[0][0] % k == 0 ? 1 : 0;
        }
        int dp[n][m][k];
        memset(dp, -1, sizeof dp);
        function<int(int, int, int)> solve = [&](int row, int col, int rem) {
            if (row < 0 || col < 0) {
                return 0;
            }
            int x = grid[row][col] % k;
            x = (rem - x + k) % k;
            if (row == 0 && col == 0) {
                return x == 0 ? 1 : 0;
            }
            int res = dp[row][col][rem];
            if (res != -1) return res;
            res = solve(row - 1, col, x);
            res += solve(row, col - 1, x);
            res %= mod;
            dp[row][col][rem] = res;
            // cout << row << " " << col << " " << rem << " " << res << endl;
            return res;
        };
        int x = (k - grid[n - 1][m - 1] % k) % k;
        int res = solve(n - 1, m - 2, x);
        res += solve(n - 2, m - 1, x);
        return res % mod;
    }
};