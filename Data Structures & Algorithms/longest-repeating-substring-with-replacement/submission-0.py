class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f = defaultdict(int)

        l = 0
        max_freq = 0
        ans = 0

        for r in range(len(s)):
            f[s[r]] += 1

            max_freq = max(max_freq, f[s[r]])

            while (r-l+1) - max_freq > k:
                f[s[l]] -= 1
                l += 1
            
            ans = max(ans, r-l+1)
        
        return ans

