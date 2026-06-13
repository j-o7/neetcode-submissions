# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:        
        if not head:
            return None
        p = None
        while head.next != None:
            nxt = head.next
            head.next = p
            p = head
            head = nxt
        
        head.next = p
        return head


        

        