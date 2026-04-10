class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n-k+1):
            ans.append(max(nums[i:i+k]))
        
        return ans