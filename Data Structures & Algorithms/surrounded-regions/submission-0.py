class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])

        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        def dfs(r, c):
            board[r][c] = '#'

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if  0<=nr<n and 0<=nc<m and board[nr][nc] == 'O':
                    dfs(nr, nc)
        
        for j in range(m):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[n-1][j] == 'O':
                dfs(n-1, j)
        
       
        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][m-1] == 'O':
                dfs(i, m-1)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                    
        for i in range(n):
            for j in range(m):
                if board[i][j] == '#':
                    board[i][j] = 'O'           