class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(r, c):
            if grid[r][c] == '1':
                grid[r][c] = '#'
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                n_r, n_c = r + dr, c + dc
                if n_r >= 0 and n_r < n and n_c >= 0 and n_c < m and grid[n_r][n_c] == '1':
                    dfs(n_r, n_c)


        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        
        return ans
        

        