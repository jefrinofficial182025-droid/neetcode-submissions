class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0 
        ans=float('inf')
        whitecount=0
        for right in range(len(blocks)): 
            if blocks[right]=='W':
                whitecount+=1
            if right-left+1>k: 
                if blocks[left]=='W':
                    whitecount-=1
                left+=1
            if right-left+1==k: 
                ans = min(ans,whitecount)
        return ans