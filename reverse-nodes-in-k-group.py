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
    def reverseKGroup_naive(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        curr = head
        stack = []
        dummy = ListNode(0)
        tail = dummy
        while curr:
            stack.append(curr)
            curr = curr.next
            if len(stack) == k:
                while stack:
                    n = stack.pop()
                    tail.next = n
                    tail = n
        if len(stack):
            for n in stack:
                tail.next = n
                tail = n
        return dummy.next
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
 
        while True:
            node = prev
            # Check if there are k nodes left to reverse
            for i in range(k):
                node = node.next
                if not node:
                    return dummy.next
 
            # Reverse k nodes
            curr = prev.next
            nex = curr.next
            for i in range(k - 1):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next
 
            prev = curr
    

head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,)))))
res = Solution().reverseKGroup(head,2)
res.print()

head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,)))))
res = Solution().reverseKGroup(head,3)
res.print()





