class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        string dir[] = {"+Y", "+X", "-Y", "-X"};
        map<int, map<int, int>> obs;
        for (auto obstacle : obstacles) {
            obs[obstacle[0]][obstacle[1]] = 1;
        }
        int res = 0;
        int cur_dir = 0;
        int cur_x = 0;
        int cur_y = 0;
        auto dist = [&] (int x, int y) {
            return x * x + y * y;
        };
        for (auto command : commands) {
            if (command == -2) { // turn left
                cur_dir = (cur_dir + 3) % 4;
            } else if (command == -1) { // turn right
                cur_dir = (cur_dir + 1) % 4;
            } else {
                if (cur_dir == 0) { // y+
                    while (command--) {
                        if (obs[cur_x][cur_y + 1] == 1) {
                            break;
                        }
                        cur_y += 1;
                        res = max(res, dist(cur_x, cur_y));
                    }
                } else if (cur_dir == 1) { //x+
                    while (command--) {
                        if (obs[cur_x + 1][cur_y] == 1) {
                            break;
                        }
                        cur_x += 1;
                        res = max(res, dist(cur_x, cur_y));
                    }
                } else if (cur_dir == 2) { // y-
                    while (command--) {
                        if (obs[cur_x][cur_y - 1] == 1) {
                            break;
                        }
                        cur_y -= 1;
                        res = max(res, dist(cur_x, cur_y));
                    }
                } else if (cur_dir == 3) { // x-
                    while (command--) {
                        if (obs[cur_x - 1][cur_y] == 1) {
                            break;
                        }
                        cur_x -= 1;
                        res = max(res, dist(cur_x, cur_y));
                    }
                } else {
                    assert(false);
                }
            }
        }
        return res;
    }
};