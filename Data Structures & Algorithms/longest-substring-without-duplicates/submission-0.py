class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,maxlength=0,0
        d={}
        for right in range(len(s)): 
            d[s[right]] = d.get(s[right],0)+1
            while d[s[right]]>1: 
                d[s[left]]-=1
                left+=1
            maxlength = max(maxlength,right-left+1)
        return maxlength