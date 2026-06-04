class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0 
        length=0
        numset = set(nums)
        maxLength = 0 
        for i in numset: 
            if i-1 not in numset: 
                length=1
                while i+1 in numset: 
                    length+=1
                    i+=1
                maxLength=max(maxLength,length)
        return maxLength