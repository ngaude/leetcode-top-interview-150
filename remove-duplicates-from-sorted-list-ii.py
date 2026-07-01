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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101,head)
        curr = head
        prev = dummy

        while curr:
            while curr.next and curr.next.val == curr.val:
                curr = curr.next  
            if prev.next == curr:
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next
      
        return dummy.next

print('---')
head = ListNode(1,ListNode(2,ListNode(2,ListNode(3,ListNode(4,ListNode(4,ListNode(5)))))))
head.print()
res = Solution().deleteDuplicates(head)
res.print()


print('---')
head = ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(4,ListNode(4,ListNode(5)))))))
head.print()
res = Solution().deleteDuplicates(head)
res.print()

print('---')
head = ListNode(1,ListNode(1,ListNode(1,ListNode(3,ListNode(4,ListNode(4,ListNode(5)))))))
head.print()
res = Solution().deleteDuplicates(head)
res.print()
