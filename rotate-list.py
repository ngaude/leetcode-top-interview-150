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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        if k == 0:
            return head
        curr = head
        last = None
        n = 0
        while curr:
            n+=1
            last = curr
            curr = curr.next
        k = k % n
        if k == 0:
            return head
        curr = head
        cut = None
        for i in range(n-k):
            cut = curr
            curr = curr.next
        cut.next = None
        last.next = head
        head = curr
        return head