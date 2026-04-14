class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            rate = (l+r) // 2

            time_taken = 0
            for p in piles:
                time_taken += (p+rate-1) // rate

            if time_taken <= h:
                ans = rate
                r = rate-1
            else:
                l = rate+1
        return ans
            

