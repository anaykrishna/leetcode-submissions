class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0

        for num in nums:
            if num-1 not in s:
                curr = num
                length = 1

                while curr + 1 in s:
                    curr += 1
                    length += 1
                
                ans = max(ans, length)
        
        return ans
        
