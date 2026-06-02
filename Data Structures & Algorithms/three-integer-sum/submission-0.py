class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i=0
        sorted_nums = sorted(nums)
        res=[]
        for i in range(len(nums)):
            if i>0 and sorted_nums[i]==sorted_nums[i-1]:
                continue

            j,k=i+1,len(nums)-1
            while j<k:
                sum = sorted_nums[i]+sorted_nums[j]+sorted_nums[k]
                if sum>0: 
                    k-=1
                elif sum<0:
                    j+=1
                else:
                    res.append([sorted_nums[i],sorted_nums[j],sorted_nums[k]])
                    j+=1
                    k-=1
                    while j<k and sorted_nums[j]==sorted_nums[j-1]:
                        j+=1
                    while j<k and sorted_nums[k]==sorted_nums[k+1]:
                        k-=1
        return res
                