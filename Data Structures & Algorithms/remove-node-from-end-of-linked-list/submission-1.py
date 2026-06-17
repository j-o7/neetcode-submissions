# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def printList(node):
    while node is not None:
        print(f"{node.val}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        f, s = head, head
        i = 0
        while f:
            print(f.val)
            if i <= n:
                f = f.next
                i += 1
                print(i)
                continue

            # if i == n:
            #     s = head
            #     f = f.next
            #     i += 1
            #     continue
            
            s = s.next
            f = f.next

        if i == n:
            return head.next
        
        s.next = s.next.next

        return head

        # First approach:
        # slow, fast = head, head
        # i, j = 0, 0
        # while fast:
        #     if not fast.next:
        #         break
        #     if not fast.next.next:
        #         fast = fast.next
        #         j += 1
        #         break

        #     slow = slow.next
        #     fast = fast.next.next
        #     i += 1
        #     j += 2
        
        # print(i)
        # print(j)
        # printList(head)
        # printList(slow.next)

        # idx = j - (n - 1)
        # print(idx)
        # if idx <= i:
        #     p, c = None, head
        #     move = idx
        # else:
        #     p, c = slow, slow.next
        #     move = idx - i - 1
        
        # while move:
        #     p = c
        #     c = c.next
        #     move -=1
        #     print(p.val)
        #     print(c.val)
        #     print(move)
        
        # if p:
        #     p.next = c.next

        # return head          
        
        