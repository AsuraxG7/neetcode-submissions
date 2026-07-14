class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=min(nums)
        n=len(nums)
        csum=0
        for i in range(n):
            csum+= nums[i]
            max_sum=max(max_sum,csum)

            if csum < 0:
               csum = 0
        return max_sum        

        