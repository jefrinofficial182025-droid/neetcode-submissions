class Solution:
    def atmost(self,nums,k):
        if k<0: 
            return 0 
        left = 0 
        winsum =0
        ans=0
        for right in range(len(nums)): 
            winsum += nums[right]
            while winsum>k: 
                winsum -= nums[left]
                left+=1
            ans += right-left+1
        return ans
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atmost(nums,goal)-self.atmost(nums,goal-1)