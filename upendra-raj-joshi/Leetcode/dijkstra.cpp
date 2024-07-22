class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        //Initialize priority queue with pairs.
        priority_queue<pair<int, pair<int, int>>,
                       vector<pair<int, pair<int, int>>>,
                       greater<pair<int, pair<int, int>>>>
            pq;
        int n = heights.size();
        int m = heights[0].size();

        //Initialize 2D vector to store distances with large initial values.
        vector<vector<int>> dis(n, vector<int>(m, 1e9));

        //Set the distance of the start point to 0 and push it into the priority queue.
        dis[0][0] = 0;
        pq.push({0, {0, 0}});

        //Possible directions ---(up, down, left, right).
        int direction[4][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

        // Dijkstra's algorithm.
        while (!pq.empty()) {
            int diff = pq.top().first;
            int x = pq.top().second.first;
            int y = pq.top().second.second;
            pq.pop();

            //Check if we have reached the target cell.
            if (x == n - 1 && y == m - 1) {
                return diff;
            }
            //Explore adjacent cells.
            for (int i = 0; i < 4; i++) {
                int newr = x + direction[i][0];
                int newc = y + direction[i][1];

                // Step 9: Check if the new position is within bounds.
                if (newr >= 0 && newc >= 0 && newr < n && newc < m) {
                    //Calculate the new effort needed which has maximum height difference.
                    int w = max(abs(heights[x][y] - heights[newr][newc]), diff);
                    //If the new effort is less than the stored distance, update and push into the queue.
                    if (w < dis[newr][newc]) {
                        dis[newr][newc] = w;
                        pq.push({w, {newr, newc}});
                    }
                }
            }
        }
        return 0;
    }
};