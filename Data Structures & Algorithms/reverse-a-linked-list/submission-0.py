# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        if head == None:
            return head

        while head.next != None:
            nxt = head.next
            head.next = p
            p = head
            head = nxt
        
        head.next = p
        return head


        

        