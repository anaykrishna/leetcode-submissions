class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = -1
            cnt = 1

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < n and nc >= 0 and nc < m and grid[nr][nc] == 1:
                    cnt += dfs(nr, nc)
            
            return cnt
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    ans = max(ans, area)
        
        return ans