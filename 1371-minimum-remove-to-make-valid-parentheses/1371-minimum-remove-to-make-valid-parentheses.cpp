class Solution {
public:
    string minRemoveToMakeValid(string s) {
        vector<int> arr, pos;
        int n = s.size();
        for (int i = 0; i < n; i++) {
            if (s[i] == '(') arr.push_back(i);
            else if (s[i] == ')') {
                if (arr.size() > 0) {
                    arr.pop_back();
                } else {
                    pos.push_back(i);
                }
            }
        }
        for (int i = 0; i < arr.size(); i++) pos.push_back(arr[i]);
        if (pos.empty()) return s;
        sort(pos.begin(), pos.end());
        int idx = 0;
        string res = "";
        for (int i = 0; i < n; i++) {
            if (idx < pos.size() && i == pos[idx]) {
                idx++;
                continue;        
            }
            res += s[i];
        }
        return res;
    }
};