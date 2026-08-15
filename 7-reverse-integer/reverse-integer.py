class Solution:
    def reverse(self, x: int) -> int:
        org=x
        if(x<0):
            x=x*-1
        rev=0
        while(x!=0):
            ans=x%10
            rev=rev*10+ans
            x=x//10
        if(org<0):
            rev=rev*-1
        if(rev<-2**31 or rev>2**31-1):
            return 0
        else:
            return rev
        return rev
    
    
        


        