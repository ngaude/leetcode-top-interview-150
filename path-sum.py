from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # dfs
        if not root:
            return False
        stack = [(root,0)]
        while stack:
            # print([(n.val,v) for n,v in stack])
            node,val = stack.pop()
            val = node.val + val
            if not node.left and not node.right:
                if val == targetSum:
                    return True
            if node.left:
                stack.append((node.left,val))
            if node.right:
                stack.append((node.right,val))
        return False


        