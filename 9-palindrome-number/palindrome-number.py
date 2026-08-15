class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        org=x
        rev=0
        while(x!=0):
            ans=x%10
            rev=rev*10+ans
            x=x//10
        if(org==rev):
           return True
        else:
            return False
        return rev
                


        