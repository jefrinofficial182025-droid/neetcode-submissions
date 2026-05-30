class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count=Counter(nums)
        d = sorted(num_count.items(), key = lambda x:x[1], reverse=True)
        list=[]
        for i in range(k): 
            list.append(d[i][0])
        return list
        