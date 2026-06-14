# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0

        cur1 = list1
        cur2 = list2

        while cur1 != None:
            n1 += 1
            cur1 = cur1.next

        while cur2 != None:
            n2 += 1
            cur2 = cur2.next

        total = n1 + n2
        i = 0
        cur1 = list1
        cur2 = list2

        # print(total)
        if n1 and n2:
            if list1.val < list2.val:
                head = cur1
                cur1 = cur1.next
                head.next = None
            else:
                head = cur2
                cur2 = cur2.next
                head.next = None
        elif n1:
            head = cur1
            cur1 = cur1.next
            head.next = None
        elif cur2:
            head = cur2
            cur2 = cur2.next
            head.next = None
        else:
            return list1

        cur = head
        i += 1
        while i < total:
            if cur1 and cur2:
                if cur1.val < cur2.val:
                    cur.next = cur1
                    cur1 = cur1.next
                    cur = cur.next
                    cur.next = None
                else:
                    cur.next = cur2
                    cur2 = cur2.next
                    cur = cur.next
                    cur.next = None
            elif cur1:
                cur.next = cur1
                cur1 = cur1.next
                cur = cur.next
                cur.next = None
            else:
                cur.next = cur2
                cur2 = cur2.next
                cur = cur.next
                cur.next = None

            i += 1

        return head
            