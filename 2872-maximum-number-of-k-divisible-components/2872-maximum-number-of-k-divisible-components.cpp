class Solution {
private:
    vector<vector<int>> adj;
    void dfs(vector<long long>& vals, int curNode, int parNode) {
        for (int i = 0; i < int(adj[curNode].size()); i++) {
            int childNode = adj[curNode][i];
            if (childNode == parNode) continue;
            dfs(vals, childNode, curNode);
            vals[curNode] += vals[childNode];
        }
    }
public:
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
        adj.resize(n);
        for (int i = 0; i < n - 1; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vector<long long> vals;
        for (int i = 0; i < n; i++) vals.push_back(values[i]);
        dfs(vals, 0, -1);
        // for (int i = 0; i < n; i++) cout << vals[i] << " "; cout << endl;
        int res = 0;
        for (int i = 0; i < n; i++) {
            if (vals[i] % k == 0) res++;
        }
        return res;
    }
};