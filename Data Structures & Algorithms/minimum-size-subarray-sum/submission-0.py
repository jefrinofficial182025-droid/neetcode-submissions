class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left =0 
        windowsum=0
        ans = float('inf')
        for right in range(len(nums)): 
            windowsum+=nums[right]
            while windowsum>=target: 
                ans = min(ans,right-left+1)
                windowsum-=nums[left]
                left+=1
        return ans if ans!=float('inf') else 0 