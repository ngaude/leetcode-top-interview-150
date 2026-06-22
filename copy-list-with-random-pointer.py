from typing import List,Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        ol = []
        n = head
        while n:
            ol.append(n)
            n = n.next
        d = {n:i for i,n in enumerate(ol)}
        cl = [Node(ol[i].val) for i in range(len(ol))]
        for i in range(len(cl)):
            if ol[i].next:
                cl[i].next = cl[d[ol[i].next]]
            if ol[i].random:
                cl[i].random = cl[d[ol[i].random]]
    
        return cl[0]
