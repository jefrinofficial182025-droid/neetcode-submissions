class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left =0 
        windowsum= 0 
        counter=0
        for right in range(len(arr)): 
            windowsum+=arr[right]
            if right-left+1>k: 
                windowsum-=arr[left]
                left+=1
            if right-left+1==k: 
                if windowsum>=threshold*k: 
                    counter+=1
        return counter