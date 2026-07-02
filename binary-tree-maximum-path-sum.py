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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # trivial 1-node path:
        ret = root.val
        maxpath = {}
        depth = {}
        stack = [(root,0)]
        while stack:
            n,d = stack.pop()
            if d in depth:
                depth[d].append(n)
            else:
                depth[d] = [n]

            if not n.right and not n.left:
                maxpath[n] = n.val
            else:
                if n.left:
                    stack.append((n.left,d+1))
                if n.right:
                    stack.append((n.right,d+1))
            
        for d in range(max(depth.keys()),-1,-1):
            if d == 0:
                pass
            for n in depth[d]:
                if n in maxpath:
                    continue
                lpath = max(maxpath.get(n.left,0),0)
                rpath = max(maxpath.get(n.right,0),0)
                if lpath + n.val + rpath > ret:
                    ret = lpath + n.val + rpath
                maxpath[n] = n.val + max(lpath,rpath)

        for n in maxpath:
            for d in depth:
                if n in depth[d]:
                    break
            # print(f'node-{n}@{d}','maxpath=',maxpath[n])
        
        return max(ret,max(maxpath.values()))

        

root = TreeNode(1,TreeNode(2),TreeNode(3))
print(root.show())
assert Solution().maxPathSum(root) == 6

root = TreeNode(-10,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
print(root.show())
assert Solution().maxPathSum(root) == 42

root = TreeNode(1,TreeNode(2))
print(root.show())
assert Solution().maxPathSum(root) == 3

root = TreeNode(5,TreeNode(4,TreeNode(11,TreeNode(7),TreeNode(2))),TreeNode(8,TreeNode(13,None,TreeNode(1)),TreeNode(4)))
print(root.show())
assert Solution().maxPathSum(root) == 49