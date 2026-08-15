class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        w=s.split()
        left=0
        right=len(w)-1
        while left<right:
            w[left],w[right]=w[right],w[left]
            left+=1
            right-=1
        return" ".join(w)

        
        