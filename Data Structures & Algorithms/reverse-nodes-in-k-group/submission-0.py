# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prevgrp = dummy
        cur = head
        length = 0 
        while cur: 
            length+=1
            cur=cur.next
        cur = head
        while length>=k: 
            grpstart = cur 
            prev = None 
            for _ in range(k): 
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            prevgrp.next = prev
            grpstart.next = cur 
            prevgrp = grpstart 
            length -= k 
        return dummy.next