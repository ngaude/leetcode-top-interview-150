# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return
        lvl = [root]
        while len(lvl):
            prev = None
            _lvl = []
            for curr in lvl:
                if prev:
                    prev.next = curr
                prev = curr
                if curr.left:
                    _lvl.append(curr.left)
                if curr.right:
                    _lvl.append(curr.right)
            lvl = _lvl
        return root

        