class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        q = deque()
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited.add((i, j))
                
        ans = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c, time = q.popleft()
            ans = time

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    visited.add((nr, nc))
                    grid[nr][nc] = 2
                    q.append((nr, nc, ans+1))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return ans  
        