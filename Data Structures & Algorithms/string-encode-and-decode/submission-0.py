class Solution:

    def encode(self, strs: List[str]) -> str:
        encstr=''
        for i in strs: 
            encstr += str(len(i)) + '#' + i 
        return encstr

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            lengthofword = int(s[i:j])
            j+=1
            word = s[j:j+lengthofword]
            ans.append(word)
            i=j+lengthofword
        return ans
        
