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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        st = [root]
        ret = 0
        while len(st) > 0:
            n = st.pop()
            ret += 1
            if n.left:
                st.append(n.left)
            if n.right:
                st.append(n.right)
        return ret