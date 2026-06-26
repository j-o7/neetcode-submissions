# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        carry = False

        total = cur1.val + cur2.val
        if total >= 10:
            res = ListNode(val = total % 10)
            carry = True
        else:
            res = ListNode(val = total)

        cur1 = cur1.next
        cur2 = cur2.next
        head = res

        while cur1 or cur2:
            if cur1:
                add1 = cur1.val
            else:
                add1 = 0
            
            if cur2:
                add2 = cur2.val
            else:
                add2 = 0

            if carry:
                total = add1 + add2 + 1
                carry = False
            else:
                total = add1 + add2

            if total >= 10:
                res.next = ListNode(val=total % 10)
                carry = True
            else:
                res.next = ListNode(val=total)

            print(res.val)
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            res = res.next

        # if cur1 and not cur2:


        if carry:
            res.next = ListNode(val = 1)
            res = res.next
        
        return head
