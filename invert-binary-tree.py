from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def _sym(left,right):
            if not left and right:
                return False
            if not right and left:
                return False
            if not right and not left:
                return True
            return (left.val == right.val) and _sym(left.left,right.right) and _sym(right.left,left.right)
        return _sym(root,root)
