class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left,have,need,countert,window,res,reslen=0,0,len(Counter(t)),Counter(t),{},[-1,-1],float('inf')
        for right in range(len(s)): 
            c = s[right]
            window[c] = window.get(c,0)+1
            if c in countert and countert[c]==window[c]:
                have+=1
            while have==need:
                if right-left+1 < reslen:
                    res=[left,right]
                    reslen=right-left+1
                window[s[left]]-=1
                if s[left] in countert and window[s[left]]<countert[s[left]]: 
                    have-=1
                left+=1
        l,r=res
        return s[l:r+1] if reslen!=float('inf') else ""