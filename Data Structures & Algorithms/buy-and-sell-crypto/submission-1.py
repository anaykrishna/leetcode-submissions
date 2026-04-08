class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_temp = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > min_temp:
                ans = max(ans, prices[i] - min_temp)
            
            if prices[i] < min_temp:
                min_temp = prices[i]
        
        return ans
