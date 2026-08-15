class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in hashmap:
                return[hashmap[comp],i]
            hashmap[nums[i]]=i



