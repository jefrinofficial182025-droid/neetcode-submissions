class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        windowsum=0
        ans=0
        for right in range(len(nums)): 
            windowsum+=nums[right]
            while nums[right]*(right-left+1)-windowsum>k:
                windowsum -= nums[left]
                left+=1
            ans = max(ans,right-left+1)
        return ans