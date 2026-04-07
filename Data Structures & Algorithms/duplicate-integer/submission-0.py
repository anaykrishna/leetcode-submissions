class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1
            if h[num] > 1:
                return True
        
        return False