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

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def __nlr(inorder,postorder):
            # inorder LNR
            # postorder LRN
        
            if len(postorder) == 0 or len(inorder) == 0:
                return (None,None,None)
        
            rootv = postorder[-1]
        
            if len(postorder) == 1 or len(inorder) == 1:
                return (TreeNode(rootv),None,None)
        
            rooti = inorder.index(rootv)

            inorder_left = inorder[:rooti]
            inorder_right= inorder[rooti+1:]

            if len(inorder_left) == 0:
                postorder_left = []
                postorder_right = postorder[:-1]
            elif len(inorder_right) == 0:
                postorder_right = []
                postorder_left = postorder[:-1]
            else:
                postorder_left = postorder[:len(inorder_left)]
                postorder_right = postorder[len(inorder_left):-1]
            print('inorder',inorder,inorder_left,inorder_right)
            print('postorder',postorder,postorder_left,postorder_right)
            assert len(postorder_left)+len(postorder_right)+1 == len(postorder)
            assert len(inorder_left)+len(inorder_right)+1 == len(inorder)
            assert len(inorder_left) == len(postorder_left)
            assert len(inorder_right) == len(postorder_right)

            return (TreeNode(rootv),(inorder_left, postorder_left),(inorder_right, postorder_right))
        
        head,left,right = __nlr(inorder,postorder)
        
        stack = []
        if left:
            stack.append((0,head,left))
        if right:
            stack.append((1,head,right))
        while stack:
            dir,n,sub = stack.pop()
            nn,left,right = __nlr(*sub)
            if dir == 0:
                n.left = nn
            else:
                n.right = nn
            if left:
                stack.append((0,nn,left))
            if right:
                stack.append((1,nn,right))
        
        return head
    
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
n = Solution().buildTree(inorder,postorder)
print(n.show())