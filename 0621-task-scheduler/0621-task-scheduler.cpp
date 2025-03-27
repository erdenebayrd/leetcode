class Solution {
public:
    
int leastInterval(vector<char>& tasks, int n) {
    int cnt[26], last[26]; n++;
        memset(cnt, 0, sizeof cnt);
        memset(last, -1, sizeof last);
        for (int i = 0; i < tasks.size(); i++) cnt[(int)(tasks[i] - 'A')]++;
        multiset<pair<int, int>> ms;
        for (int i = 0; i < 26; i++) {
            if (cnt[i] == 0) continue;
            ms.insert({-cnt[i], i});
        }
        vector<int> res;
        while (!ms.empty()) {
            // for (auto it : ms) cout << it.first << " " << it.second << endl;
            int sz = 0;
            multiset<pair<int, int>> dl;
            for (auto it : ms) {
                if (sz >= n) break;
                pair<int, int> cur = it;
                int ch = cur.second;
                while (last[ch] != -1 && res.size() - last[ch] < n) res.push_back(-1);
                last[ch] = res.size();
                res.push_back(ch);
                dl.insert(cur);
                sz++;
            }
            for (auto it : dl) {
                pair<int, int> cur = it;
                ms.erase(ms.find(cur));
                if (cur.first < -1) ms.insert({cur.first + 1, cur.second});
            }
        }
        // for (auto i : res) cout << i << " "; cout << endl;
        return res.size();
    }
};