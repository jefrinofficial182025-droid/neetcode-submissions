# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge(self,list1,list2): 
        dummyNode = ListNode(); 
        copy = dummyNode
        while list1 and list2: 
            if list1.val>list2.val: 
                copy.next=list2
                list2=list2.next
            else: 
                copy.next=list1
                list1=list1.next
            copy = copy.next 
        if list1: 
            copy.next=list1
        if list2: 
            copy.next =list2
        return dummyNode.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0: 
            return None 
        while len(lists)>1: 
            temp = [] 
            for i in range(0,len(lists),2): 
                list1,list2=lists[i],lists[i+1] if i+1<len(lists) else None
                temp.append(self.merge(list1,list2))
            lists=temp
        return lists[0]
                
        
