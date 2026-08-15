class Solution:
    def makeGood(self, s: str) -> str:
        st=[]
        for i in s:
            if st!=[] and i!=st[-1] and i.lower()==st[-1].lower():
                st.pop()
            else:
                st.append(i)
        return"".join(st)
        
        