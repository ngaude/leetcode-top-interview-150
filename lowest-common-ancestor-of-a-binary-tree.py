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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {}
        stack = [root]
        pfound = False
        qfound = False
        while (not pfound) or (not qfound):
            n = stack.pop()
            if n == p:
                pfound = True
            if n == q:
                qfound = True
            if n.left:
                parent[n.left] = n
                stack.append(n.left)
            if n.right:
                parent[n.right] = n
                stack.append(n.right)
    
        visited = set((p,q))
        
        while True:
            if p in parent:
                p = parent[p]
                if p in visited:
                    return p
                else:
                    visited.add(p)
            if q in parent:
                q = parent[q]
                if q in visited:
                    return q
                else:
                    visited.add(q)

root = TreeNode(3,TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4))),TreeNode(1,TreeNode(0),TreeNode(8)))
p  = root.left
q =  root.left.right.right
print(root.show())
print('p=',p.val,'q=',q.val)
lca = Solution().lowestCommonAncestor(root,p,q)
assert lca.val == 5
