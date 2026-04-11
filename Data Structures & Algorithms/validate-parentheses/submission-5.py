class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        d = {"(":")", "[":"]", "{":"}"}
        st = []

        for c in s:
            if c in d:
                st.append(c)
            else:
                if not st or d[st[-1]] != c:
                    return False
                st.pop()
        
        return len(st) == 0
