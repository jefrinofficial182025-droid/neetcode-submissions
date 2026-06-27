# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        length=0
        if not head: 
            return None
        if not head.next: 
            return None
        while cur: 
            length+=1
            cur=cur.next
        targetValue=length-n
        if targetValue==0: 
            return head.next
        prev=None
        cur=head
        counter=0
        while cur:
            if counter==targetValue:
                prev.next=cur.next
                break
            counter+=1
            prev=cur
            cur=cur.next
        return head

