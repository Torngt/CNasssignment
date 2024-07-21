
class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int rows = heights.size();
        int cols = heights[0].size();
        vector<vector<int>> dp(rows, vector<int>(cols, INT_MAX));
        vector<vector<int>> dir = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };

        dp[0][0] = 0;
        bool relaxAtleastOneEdge = true;

        for (int e = 0; e < (rows * cols) - 1 && relaxAtleastOneEdge; e++) {
            relaxAtleastOneEdge = false;

            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    for (int k = 0; k < 4; k++) {
                        int newI = i + dir[k][0];
                        int newJ = j + dir[k][1];

                        if (newI < 0 || newI >= rows || newJ < 0 || newJ >= cols || dp[i][j] >= dp[newI][newJ])
                            continue;

                        int absDiff = abs(heights[newI][newJ] - heights[i][j]);

                        if (dp[newI][newJ] > max(dp[i][j], absDiff)) {
                            dp[newI][newJ] = max(dp[i][j], absDiff);
                            relaxAtleastOneEdge = true;
                        }
                    }
                }
            }
        }

        return dp[rows - 1][cols - 1];
    }
};

/*
//*Problem Summary
Given a 2D grid of heights, the goal is to find a path from the top-left corner to the bottom-right corner such that the maximum difference in heights between consecutive cells in the path is minimized.

//* Solution Approach
This problem can be solved using a modified version of the Bellman-Ford algorithm, which is typically used to find the shortest paths in graphs with negative weights. In this case, we adapt it to find the path with the minimum effort, where effort is defined as the maximum height difference between adjacent cells.

Detailed Explanation
//*Initialization:


int rows = heights.size();
int cols = heights[0].size();
vector<vector<int>> dp(rows, vector<int>(cols, INT_MAX));
vector<vector<int>> dir = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };
rows and cols store the dimensions of the heights matrix.
dp is a 2D vector initialized to INT_MAX, representing the minimum effort required to reach each cell.
dir is a 2D vector containing the possible directions of movement (right, down, left, up).


//*Setting the Start Point:
dp[0][0] = 0;
The starting point (top-left cell) has an effort of 0 since there's no movement yet.

//*Relaxation Loop:
bool relaxAtleastOneEdge = true;

for (int e = 0; e < (rows * cols) - 1 && relaxAtleastOneEdge; e++) {
    relaxAtleastOneEdge = false;
A boolean flag relaxAtleastOneEdge is used to check if any updates were made in the current iteration.
The outer loop runs up to (rows * cols) - 1 times, which is the maximum number of edges to be relaxed in a Bellman-Ford algorithm. It stops early if no updates are made in an iteration.

//*Relaxing All Edges:
for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
        for (int k = 0; k < 4; k++) {
            int newI = i + dir[k][0];
            int newJ = j + dir[k][1];

            if (newI < 0 || newI >= rows || newJ < 0 || newJ >= cols || dp[i][j] >= dp[newI][newJ])
                continue;

            int absDiff = abs(heights[newI][newJ] - heights[i][j]);

            if (dp[newI][newJ] > max(dp[i][j], absDiff)) {
                dp[newI][newJ] = max(dp[i][j], absDiff);
                relaxAtleastOneEdge = true;
            }
        }
    }
}
The nested loops iterate over all cells and their possible movements.
For each cell (i, j), the inner loop checks all four possible directions (right, down, left, up).
It calculates the new coordinates newI and newJ for the adjacent cell.
If the new coordinates are out of bounds or if moving to the new cell does not reduce the effort, the loop continues.
The absolute difference in heights between the current cell and the adjacent cell is calculated as absDiff.
If the effort to reach the adjacent cell can be reduced by taking the current path, the dp value for the adjacent cell is updated, and the flag relaxAtleastOneEdge is set to true.


//*Returning the Result:
return dp[rows - 1][cols - 1];
The minimum effort required to reach the bottom-right cell (rows - 1, cols - 1) is returned.

//*Conclusion
This approach ensures that we find the path with the minimum effort by iteratively relaxing the edges and updating the effort required to reach each cell. The use of the Bellman-Ford-like relaxation technique helps in handling the problem efficiently by stopping early if no further relaxation is possible.

*/