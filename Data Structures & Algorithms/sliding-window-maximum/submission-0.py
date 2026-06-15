class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left=0
        res=[]
        for right in range(len(nums)): 
            if right-left+1>k: 
                left+=1
            if right-left+1==k: 
                res.append(max(nums[left:right+1]))
        return res