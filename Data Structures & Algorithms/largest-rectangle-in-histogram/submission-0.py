class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        maxA = 0
        heights.append(0)

        for i in range(len(heights)):
            while st and heights[st[-1]] > heights[i]:
                h = heights[st.pop()]

                if st:
                    w = i - st[-1] - 1
                else:
                    w = i
                
                maxA = max(maxA, h*w)
 
            st.append(i)
        
        return maxA