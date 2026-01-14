class Solution {
    using ll = long long;
    // Special coverage segment tree
    // Key points: It is not tranditional segment tree since the input is <+1 -1> pair. 
    // Each node mean a x segment, if xSet = [0, 1 ,3], then we have two node with length [1, 2] 
    // It record the length of x segment, cover count, actually length (only use when cover count = 0)  
    // Use 0-indexed with 2*i+1 and 2*i+2
    class SegmentTree{
        int n; // node range: 0~n-1
        vector<int> coverNum;
        vector<int> curLen;
        vector<int> len;
        void build(int node, int l, int r, const vector<int>& xPos){
            if(l == r){
                len[node] = xPos[l+1] - xPos[l]; // the legnth of lth segment
                return;
            }
            int mid = (l + r) / 2;
            build(2*node+1, l, mid, xPos);
            build(2*node+2, mid+1, r, xPos);
            len[node] = len[2*node+1] + len[2*node+2];
        }
        void update(int node, int l, int r, int ql, int qr, int val){
            if(qr < l || r < ql) return;
            // speaical case in this special tree
            else if(ql <= l && r <= qr) coverNum[node] += val; 
            else {
                int mid = (l + r) / 2;
                update(2*node+1, l, mid, ql, qr, val);
                update(2*node+2, mid+1, r, ql, qr, val);
            }

            if(coverNum[node] > 0) curLen[node] = len[node];
            else {
                if(l == r) curLen[node] = 0;
                else curLen[node] = curLen[2*node+1] + curLen[2*node+2];
            }
        }
    public:
        SegmentTree(const vector<int>& xPos){
            n = xPos.size() - 1; // record segment instead of point
            coverNum.resize(4*n);
            curLen.resize(4*n);
            len.resize(4*n);
            build(0, 0, n-1, xPos);
        }
        // only query whole x-axis in this case
        int query(){
            return curLen[0];
        }
        void update(int lInd, int rInd, int val){
            update(0, 0, n-1, lInd, rInd-1, val);
        }
    };
public:
    double separateSquares(vector<vector<int>>& squares) {
        // 1. Change the squares meaning to a line [x, y, +-l]
        int squSize = squares.size();
        squares.reserve(2 * squSize);
        set<int> xSet;
        for(int i=0; i<squSize; ++i){
            squares.push_back(squares[i]);
            squares.back()[1] += squares.back()[2];
            squares.back()[2] *= -1;
            xSet.insert(squares[i][0]);
            xSet.insert(squares[i][0] + squares[i][2]);
        }
        // 2. xPos index for mapping to segment tree index
        vector<int> xPos(xSet.begin(), xSet.end());
        sort(squares.begin(), squares.end(), [&](vector<int>& a, vector<int>& b){
            return a[1] < b[1];
        });
        
        // area[i] means the total area from between line[0] ~ line[i]
        int n = squares.size();
        vector<ll> area(n, 0); 
        SegmentTree segmentTree(xPos);
        // 3 and 4: Line sweep + segment tree
        for(int i=0; i<n-1; ++i){
            auto& line = squares[i];
            int start = line[0], end = line[0] + abs(line[2]);
            int sInd = lower_bound(xPos.begin(), xPos.end(), start) - xPos.begin();
            int eInd = lower_bound(xPos.begin(), xPos.end(), end) - xPos.begin();
            int y = line[1];
            int height = squares[i+1][1] - squares[i][1]; // width from segment tree

            // Update segment tree and then get the correct width between line[i] and line[i+1]
            segmentTree.update(sInd, eInd, line[2] > 0 ? 1 : -1);
            int width = segmentTree.query();
            area[i+1] = area[i] + 1LL * width * height; 
        }
        
        // Find the first line that make the area >= target, guarantee ind > 0
        // And then use interpolation
        ll target = (area.back() + 1) / 2;
        int ind = lower_bound(area.begin(), area.end(), target) - area.begin();
        double ratio = (0.5 * area.back() - area[ind-1]) / (area[ind] - area[ind-1]);
        return squares[ind-1][1] + (squares[ind][1] - squares[ind-1][1]) * ratio;
    }
};