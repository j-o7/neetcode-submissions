# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head


        # printList(head)
        l1 = head
        l2 = head
        i = 0
        j = 0

        while l1 and l2:
            if not l2.next:
                break

            if not l2.next.next:
                l2 = l2.next
                j += 1
                break

            l1 = l1.next
            i += 1

            l2 = l2.next.next
            j += 2    

        p, c = None, l1.next
        l1.next = None
        while c:
            nxt = c.next
            c.next = p
            p = c
            c = nxt

        c1 = head
        c2 = l2
        while c1:
            if not c2:
                break

            nxt1 = c1.next
            nxt2 = c2.next
            c1.next = c2
            c2.next = nxt1
            c1 = nxt1
            c2 = nxt2
        