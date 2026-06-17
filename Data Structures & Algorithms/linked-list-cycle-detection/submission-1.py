# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        one_skip = head
        two_skip = head

        while True:
            if not one_skip:
                return False
            
            if not two_skip:
                return False

            one_skip = one_skip.next

            if not two_skip.next:
                return False
            
            two_skip = two_skip.next.next

            if one_skip is two_skip:
                return True
            print(one_skip)
            print(two_skip)