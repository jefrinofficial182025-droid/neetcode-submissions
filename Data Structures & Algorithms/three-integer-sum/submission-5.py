class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i=0
        ans=[]
        sortedlist=sorted(nums)
        for i in range(len(nums)):
            if i>0 and sortedlist[i-1]==sortedlist[i]:
                continue
            j,k=i+1,len(nums)-1
            while j<k:
                sum = sortedlist[i]+sortedlist[j]+sortedlist[k]
                if sum>0:
                    k-=1
                elif sum<0:
                    j+=1
                else: 
                    ans.append([sortedlist[i],sortedlist[j],sortedlist[k]])
                    j+=1
                    k-=1
                    while j<k and sortedlist[j]==sortedlist[j-1]:
                        j+=1
                    while j<k and sortedlist[k]==sortedlist[k+1]:
                        k-=1
        return ans