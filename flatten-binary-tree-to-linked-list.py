from typing import Optional,List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

    def show(self, level=0):
        ret = "\t"*level + repr(self.val) + "\n"
        if self.left:
            ret += self.left.show(level + 1)
        else:
            ret += "\t"* (level+1) + "null\n"
        if self.right:
            ret += self.right.show(level + 1)
        else:
            ret += "\t"* (level+1) + "null\n"
        return ret

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None
        ll = []
        stack = [root]
        while len(stack):
            n = stack.pop()
            ll.append(n)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)
        print('->'.join([str(n) for n in ll]))
        prev = None
        for curr in ll:
            if prev:
                prev.right = curr
                prev.left = None
            prev = curr
        prev.right = None
        prev.left = None
        


n = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,None,TreeNode(6)))
print(n.show())
Solution().flatten(n)
print(n.show())