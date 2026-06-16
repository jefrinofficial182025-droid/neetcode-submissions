class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: 
            return 0 
        left = 0 
        windowpdt = 1
        ans = 0 
        for right in range(len(nums)): 
            windowpdt*=nums[right]
            while windowpdt>=k: 
                windowpdt//=nums[left]
                left+=1
            ans += right-left+1
        return ans