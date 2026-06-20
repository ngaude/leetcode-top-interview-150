from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if not head:
            return False
        if head.next:
            fast = head.next
        else:
            return False
        while fast and slow:
            if fast == slow and fast and slow:
                return True
            if fast:
                fast = fast.next
                if fast == slow  and fast and slow:
                    return True
                if fast:
                    fast = fast.next
                    if fast == slow  and fast and slow:
                        return True
            if slow:
                slow = slow.next
        return False