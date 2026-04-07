class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for i in range(n)]
        ans = s[0]
        for i in range(n):
            dp[i][i] = True
            if i < n-1 and s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = s[i:i+2]
            

        for curr_len in range(3, n+1):
            for j in range(0, n-curr_len+1):
                if s[j] == s[j+curr_len-1] and dp[j+1][j+curr_len-2] == True:
                    dp[j][j+curr_len-1] = True
                    if curr_len > len(ans):
                        ans = s[j:j+curr_len]

        return ans