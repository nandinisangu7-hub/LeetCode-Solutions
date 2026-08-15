class Solution:
    def removeStars(self, s: str) -> str:
        st=[]
        for i in s:
            if i!="*":
                st.append(i)
            else:
                st.pop()
        return "".join(st)
        