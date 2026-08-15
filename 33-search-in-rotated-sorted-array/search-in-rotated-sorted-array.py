class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if(nums[mid]==target):
                return mid
            #left half sorted
            elif nums[left]<=nums[mid]:
                if nums[left]<=target and target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            
            #right half sorted
            elif nums[right]>=nums[mid]:
                if nums[right]>=target and target>=nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
      
