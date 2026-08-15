class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        res=0
        while(left<=right):
            mid=(left+right)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                right=mid-1
            else:
                res=mid+1
                left=mid+1
        return res
        