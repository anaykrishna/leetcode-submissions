class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        n = len(temperatures)
        ans = [0] * n
        

        for i in range(n):
            while st and temperatures[i] > temperatures[st[-1]]:
                index = st.pop()
                ans[index] = i - index

            st.append(i)
        
        return ans
            
            
