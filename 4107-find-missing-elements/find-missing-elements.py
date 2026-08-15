class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s=set(nums)
        mn,mx=min(s),max(s)
        r=[]
        for x in range(mn+1,mx):
            if x not in s:
                r.append(x)
        return r
        
        