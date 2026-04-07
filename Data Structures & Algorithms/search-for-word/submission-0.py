class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(word)
        n = len(board)
        m = len(board[0])
        def helper(r, c, ind):
            if ind == l:
                return True
            
            if r >= n or r < 0 or c >= m or c < 0:
                return False
            
            if board[r][c] == word[ind]:
                temp = board[r][c]
                board[r][c] = '#'
                res = helper(r+1, c, ind+1) or helper(r-1, c, ind+1) or helper(r, c+1, ind+1) or helper(r, c-1, ind+1)
                board[r][c] = temp
                return res
            else:
                return False
        
        for i in range(n):
            for j in range(m):
                if helper(i, j, 0):
                    return True
        return False