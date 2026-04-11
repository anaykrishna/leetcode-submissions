class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        st = []
        arith = {"+", "-", "*", "/"}

        for c in tokens:
            if c not in arith:
                st.append(int(c))
            else:   #check is st is empty
                op2 = st.pop()
                op1 = st.pop()

                if c == "+":
                    st.append(op1 + op2)
                elif c == "-":
                    st.append(op1 - op2)
                elif c == "*":
                    st.append(op1 * op2)
                else: 
                    st.append(int(op1 / op2))
        return st[0]