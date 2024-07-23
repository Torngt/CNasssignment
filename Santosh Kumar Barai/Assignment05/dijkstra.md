# LeetCode Problems and Solutions

## Problem 1: Network Delay Time (Dijkstra's Algorithm)

**Problem Statement**:
You are given a network of `n` nodes, where each node is connected by directed edges with a certain weight (time). The task is to find the time it takes for a signal to travel from a source node to all other nodes in the network. If some nodes are unreachable, return `-1`.

**LeetCode Link**: [Network Delay Time](https://leetcode.com/problems/network-delay-time/)

### Solution Using Dijkstra's Algorithm

**C++ Code**:
```cpp
#include <vector>
#include <queue>
#include <climits>

using namespace std;

int networkDelayTime(vector<vector<int>>& times, int n, int k) {
    // Create the adjacency list
    vector<vector<pair<int, int>>> graph(n + 1);
    for (const auto& time : times) {
        int u = time[0], v = time[1], w = time[2];
        graph[u].emplace_back(v, w);
    }
    
    // Initialize distances with infinity
    vector<int> dist(n + 1, INT_MAX);
    dist[k] = 0;
    
    // Min-heap priority queue
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> minHeap;
    minHeap.emplace(0, k);
    
    while (!minHeap.empty()) {
        int u = minHeap.top().second;
        int d = minHeap.top().first;
        minHeap.pop();
        
        if (d > dist[u]) continue;
        
        for (const auto& [v, w] : graph[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                minHeap.emplace(dist[v], v);
            }
        }
    }
    
    // Find the maximum delay time
    int maxTime = 0;
    for (int i = 1; i <= n; ++i) {
        if (dist[i] == INT_MAX) return -1; // Some nodes are unreachable
        maxTime = max(maxTime, dist[i]);
    }
    
    return maxTime;
}
```


## Problem 2: Shortest Path in a Weighted Grid (Bellman-Ford Algorithm)

**Problem Statement**:
You are given a weighted grid where each cell in the grid represents a cost to enter that cell. You need to find the shortest path from the top-left corner to the bottom-right corner of the grid. You can move to adjacent cells in the grid (up, down, left, right). If there is no path from the start to the end, return `-1`.

**LeetCode Link**: [Shortest Path in a Weighted Grid](https://leetcode.com/problems/shortest-path-in-a-weighted-grid/)

### Solution Using Bellman-Ford Algorithm

The Bellman-Ford algorithm is useful here because it can handle graphs with negative weights and can be used to find the shortest paths in a weighted grid. 

**C++ Code**:
```cpp
#include <vector>
#include <climits>

using namespace std;

int shortestPathInGrid(int m, int n, vector<vector<int>>& grid) {
    // Directions for moving in the grid: right, down, left, up
    vector<vector<int>> directions{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    
    // Initialize distance matrix
    vector<vector<int>> dist(m, vector<int>(n, INT_MAX));
    dist[0][0] = grid[0][0];
    
    // Relaxation for (m * n - 1) times
    for (int k = 0; k < m * n - 1; ++k) {
        bool updated = false;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                for (const auto& dir : directions) {
                    int ni = i + dir[0];
                    int nj = j + dir[1];
                    if (ni >= 0 && ni < m && nj >= 0 && nj < n && dist[i][j] != INT_MAX) {
                        if (dist[i][j] + grid[ni][nj] < dist[ni][nj]) {
                            dist[ni][nj] = dist[i][j] + grid[ni][nj];
                            updated = true;
                        }
                    }
                }
            }
        }
        if (!updated) break;
    }
    
    // Return the shortest path to the bottom-right corner
    return dist[m - 1][n - 1] == INT_MAX ? -1 : dist[m - 1][n - 1];
}