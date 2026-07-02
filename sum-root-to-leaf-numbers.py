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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        stack = [(root,0)]
        while stack:
            n,val = stack.pop()
            val = n.val + val*10
            if n.left:
                stack.append((n.left,val))
            if n.right:
                stack.append((n.right,val))
            if not n.left and not n.right:
                total +=  (val)
        return total

root = TreeNode(1,TreeNode(2),TreeNode(3))
assert Solution().sumNumbers(root) == 25

root = TreeNode(4,TreeNode(9,TreeNode(5),TreeNode(1)),TreeNode(0))
print(root.show())
assert Solution().sumNumbers(root) == 1026