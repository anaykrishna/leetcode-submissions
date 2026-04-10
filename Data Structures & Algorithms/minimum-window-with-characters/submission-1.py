class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        need = Counter(t)
        need_len = len(need)
        have = 0

        res = [-1, -1]
        res_len = float("inf")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1
            
            while have == need_len:
                if (r-l+1) < res_len:
                    res = [l, r]
                    res_len = r-l+1
                
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0]: res[1]+1]