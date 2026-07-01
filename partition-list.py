from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):
        curr = self
        s = []
        while curr and len(s) < 100:
            s.append(str(curr.val))
            curr = curr.next
        print('->'.join(s))

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head
        hmin = ListNode(0)
        hmax = ListNode(0)
        prevmin = hmin
        prevmax = hmax
        while curr:
            if curr.val < x:
                prevmin.next = curr
                prevmin = curr
            else:
                prevmax.next = curr
                prevmax = curr
            curr = curr.next
        prevmin.next = hmax.next
        prevmax.next = None
        return hmin.next

print('---')
head = ListNode(1,ListNode(4,ListNode(3,ListNode(2,ListNode(5,ListNode(2))))))
head.print()
res = Solution().partition(head,3)
res.print()
