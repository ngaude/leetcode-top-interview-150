from typing import Optional,List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

    def show(self, level=0,isleft=True):
        ret = ''
        if self.right:
            ret += self.right.show(level + 1,True)
        
        ret += '   '*level + ('--' if level==0 else ("/-" if isleft  else "\\-")) + ">" + repr(self.val) + "\n"
        if self.left:
            ret += self.left.show(level + 1,False)
        return ret

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        ret = []
        odd = False
        while len(stack)>0:
            v = [n.val for n in stack]
            if odd:
                v = v[::-1]
            odd = not odd
            ret.append(v)
            _stack = []
            for n in stack:
                if n.left:
                    _stack.append(n.left)
                if n.right:
                    _stack.append(n.right)
            stack = _stack
        return ret