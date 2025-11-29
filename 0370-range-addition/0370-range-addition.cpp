class Solution {
public:
    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
        vector<int> arr(length + 1, 0);
        for(int i = 0; i < updates.size(); i++) {
            int stIdx = updates[i][0];
            int edIdx = updates[i][1];
            int inc = updates[i][2];
            arr[stIdx] += inc;
            arr[edIdx + 1] -= inc;
        }
        for (int i = 1; i < length; i++) arr[i] += arr[i - 1];
        arr.resize(length);
        return arr;
    }
};