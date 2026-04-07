class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        n, m = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_h):
            if (r, c) in visited or r < 0 or r >= n or c < 0 or c >= m:
                return
            
            if heights[r][c] < prev_h:
                return
            
            visited.add((r, c))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                dfs(r+dr, c+dc, visited, heights[r][c])

        
        for i in range(n):
            dfs(i, 0, pacific, 0) 
        for j in range(m):
            dfs(0, j, pacific, 0)  
        
        for i in range(n):
            dfs(i, m - 1, atlantic, 0) 
        for j in range(m):
            dfs(n - 1, j, atlantic, 0)
        
        return list(pacific & atlantic)