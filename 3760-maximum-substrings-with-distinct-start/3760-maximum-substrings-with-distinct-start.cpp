class Solution {
public:
    int maxDistinct(string s) {
        set<char> st;
        for (auto ch: s) st.insert(ch);
        return st.size();
    }
};