class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        br={')':'(','}':'{',']':'['}
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                if st==[] or br[i]!=st[-1]:
                    return False
                st.pop()
        if st==[]:
            return True 
        else:
            return False