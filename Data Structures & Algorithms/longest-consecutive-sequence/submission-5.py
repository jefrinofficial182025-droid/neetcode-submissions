class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        numset = set(nums) 
        longest = 0 
        length = 0
        for i in numset: 
            if i-1 not in numset: 
                length = 1
                while i+1 in numset: 
                    length+=1
                    i+=1
                longest = max(longest,length)
        return longest