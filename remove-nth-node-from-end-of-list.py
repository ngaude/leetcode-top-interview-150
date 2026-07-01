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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy
        late = dummy
        i = 0
        while curr.next:
            i+=1
            if i > n:
                late = late.next
            curr = curr.next
        late.next = late.next.next
        return dummy.next
    
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,)))))
res = Solution().removeNthFromEnd(head,2)
res.print()

head = ListNode(1,ListNode(2))
res = Solution().removeNthFromEnd(head,2)
res.print()

