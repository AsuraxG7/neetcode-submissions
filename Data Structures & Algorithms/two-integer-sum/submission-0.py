class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      hm={}
      n=len(nums)
      for i in range(n):
        rem=target-nums[i]
        if rem in hm:
            return [hm[rem], i]

        hm[nums[i]]=i    


