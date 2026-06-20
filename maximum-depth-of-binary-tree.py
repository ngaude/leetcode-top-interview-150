# Definition for a binary tree node.
from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        dmax = 0
        stack = [(root,1)]
        while len(stack):
            curr,d = stack.pop()
            if d > dmax:
                dmax = d
            if curr.left:
                stack.append((curr.left,d+1))
            if curr.right:
                stack.append((curr.right,d+1))
        return dmax

root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
print(Solution().maxDepth(root))