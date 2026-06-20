from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        tail = None 
        while l1 or l2:
            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
            l = ListNode((v1+v2+carry)%10)
            if head is None:
                head = l
                tail = l
            else:
                tail.next = l
                tail = l
            carry = (v1+v2+carry)//10
        if carry > 0:
            l = ListNode(1)
            tail.next = l
        return head


def llist(l):
    v = []
    while l:
        v.append(l.val)
        l = l.next
    return(v)

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))
l = Solution().addTwoNumbers(l1,l2)
print('l1',llist(l1))
print('l2',llist(l2))
print('l',llist(l))


l1 = ListNode(9,ListNode(9))
l2 = ListNode(9)
l = Solution().addTwoNumbers(l1,l2)
print('l1',llist(l1))
print('l2',llist(l2))
print('l',llist(l))

