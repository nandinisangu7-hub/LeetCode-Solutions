class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if i in "+-*/":
                t1=st.pop()
                t2=st.pop()
                if i=="+":
                    st.append(t2+t1)
                elif i=="-":
                    st.append(t2-t1)
                elif i=="*":
                    st.append(t2*t1)
                else:
                    st.append(int(t2/t1))
            else:
                st.append(int(i))
        return st[-1]
        