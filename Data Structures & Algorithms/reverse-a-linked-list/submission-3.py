# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
        # p = None
        # if head == None:
        #     return head

        # while head.next != None:
        #     nxt = head.next
        #     head.next = p
        #     p = head
        #     head = nxt
        
        # head.next = p
        # return head


        

        