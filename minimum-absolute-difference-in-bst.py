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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        n = root
        ret = 10**5
        while n:
            stack.append(n)
            n = n.left
        pval = None
        while len(stack):
            n = stack.pop()
            val = n.val
            
            if pval != None:
                diff = abs(pval-val)
                if diff < ret:
                    ret = diff
            pval = val
            
            if n.right:
                n = n.right
                while n:
                    stack.append(n)
                    n = n.left
            
            
        return ret

root = TreeNode(236,TreeNode(104,None,TreeNode(227)),TreeNode(701,None,TreeNode(911)))
print(root.show())
assert Solution().getMinimumDifference(root) == 9


root = TreeNode(0,None,TreeNode(2236,TreeNode(1277,TreeNode(519),None),TreeNode(2776)))
print(root.show())
assert Solution().getMinimumDifference(root) == 519
