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
    def kthSmallest(self, root: Optional[TreeNode],k: int) -> int:
        stack = []
        n = root
        while n:
            stack.append(n)
            n = n.left
        while len(stack) and k:
            n = stack.pop()
            val = n.val
            k-=1
            if n.right:
                n = n.right
                while n:
                    stack.append(n)
                    n = n.left            
            
        return val


root = TreeNode(3,TreeNode(1,None,TreeNode(2)),TreeNode(4))
print(root.show())
assert Solution().kthSmallest(root,1) == 1

root = TreeNode(5,TreeNode(3,TreeNode(2,TreeNode(1)),TreeNode(4)),TreeNode(6))
print(root.show())
assert Solution().kthSmallest(root,3) == 3
