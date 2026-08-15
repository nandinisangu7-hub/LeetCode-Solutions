class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=set(nums)
        for x in range(len(n)+1):
            if x not in n:
                return x

