from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        curr = head
        pos = 1
        stack = []
        start = None
        while curr:
            if pos == left-1:
                start = curr
            elif pos >= left and pos < right:
                stack.append(curr)
            elif pos == right:
                if start:
                    start.next = curr
                    end = curr.next
                    start = start.next
                else:
                    head = curr
                    start = curr
                    end = curr.next
                while stack:
                    n = stack.pop()
                    if start:
                        start.next = n
                    start = n
                curr = start
                curr.next = end
            prev = curr
            if curr:
                curr = curr.next
                pos +=1
        return head
    
a = [ListNode(i) for i in range(1,6)]
for i in range(0,4):
    a[i].next = a[i+1]
head = a[0]
res = Solution().reverseBetween(head,2,4)
val = []
while res:
    val.append(res.val)
    res = res.next 
assert val == [1,4,3,2,5]

head = ListNode(5)
res = Solution().reverseBetween(head,1,1)
val = []
while res:
    val.append(res.val)
    res = res.next 
assert val == [5]

head = ListNode(3,ListNode(5))
res = Solution().reverseBetween(head,2,2)
val = []
while res:
    val.append(res.val)
    res = res.next 
assert val == [3,5]


head = ListNode(3,ListNode(5))
res = Solution().reverseBetween(head,1,2)
val = []
while res:
    val.append(res.val)
    res = res.next 
assert val == [5,3]