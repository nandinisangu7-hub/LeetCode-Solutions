class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        chunty=0
        bunty=len(nums)-1
        punty=0
        while(punty<=bunty):
            if(nums[punty]==0):
                (nums[chunty],nums[punty])=(nums[punty],nums[chunty])
                chunty+=1
                punty+=1
            elif (nums[punty]==2):
                (nums[bunty],nums[punty])=(nums[punty],nums[bunty])
                bunty-=1
            else:
                punty+=1
            