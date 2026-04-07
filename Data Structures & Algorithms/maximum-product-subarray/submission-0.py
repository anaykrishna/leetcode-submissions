class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        Max, Min = 1, 1

        for num in nums:
            temp = num*Max
            Max = max(num*Max, num*Min, num)
            Min = min(temp, num*Min, num)
            ans = max(ans, Max)
        
        return ans