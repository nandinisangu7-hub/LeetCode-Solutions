class Solution:
    def isHappy(self, n: int) -> bool:
        emptyset=set()
        while(n!=0 and n not in emptyset):
            emptyset.add(n)
            sum=0
            while(n!=0):
                dig=n%10
                sum=sum+dig**2
                n=n//10
            n=sum
        return n==1

                                      