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
    def buildTree_naive(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
        # preorder NLR
        # inorder LNR
    
        if len(preorder) == 0 or len(inorder) == 0:
            return None
    
        rootv = preorder[0]
    
        if len(preorder) == 1 or len(inorder) == 1:
            return TreeNode(rootv)
    
        rooti = inorder.index(rootv)
        inorder_left = inorder[:rooti]
        inorder_right= inorder[rooti+1:]
        preorder_left = [i for i in preorder if i in inorder_left]
        preorder_right = [i for i in preorder if i in inorder_right]
        left = self.buildTree(preorder_left, inorder_left)
        right = self.buildTree(preorder_right, inorder_right)
        
        return TreeNode(rootv,left,right)


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def __nlr(preorder,inorder):
            # preorder NLR
            # inorder LNR

            if len(preorder) == 0 or len(inorder) == 0:
                return (None,None,None)
    
            rootv = preorder[0]
    
            if len(preorder) == 1 or len(inorder) == 1:
                return (TreeNode(rootv),None,None)
        
            rooti = inorder.index(rootv)

            if len(preorder) == 2 or len(inorder) == 2:
                if rooti == 0:
                    # no left...
                    rightv = inorder[1]
                    return (TreeNode(rootv,left=None,right=TreeNode(rightv)),None,None)
                else:
                    # ni right...
                    leftv = inorder[0]
                    return (TreeNode(rootv,left=TreeNode(leftv),right=None),None,None)

            inorder_left = inorder[:rooti]
            inorder_right= inorder[rooti+1:]

            if len(inorder_left) == 0:
                preorder_left = []
                preorder_right = preorder[1:]
            elif len(inorder_right) == 0:
                preorder_right = []
                preorder_left = preorder[1:]
            else:
                
                preorder_left = preorder[1:1+len(inorder_left)]
                preorder_right = preorder[1+len(inorder_left):]

            return (TreeNode(rootv),(preorder_left, inorder_left),(preorder_right, inorder_right))
        
        head,left,right = __nlr(preorder,inorder)
        
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

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# n = Solution().buildTree(preorder,inorder)
# print(n.show())

# preorder = [1,2,3]
# inorder = [3,2,1]
# n = Solution().buildTree(preorder,inorder)
# print(n.show())


# preorder = [1,2,3]
# inorder = [2,3,1]
# n = Solution().buildTree(preorder,inorder)
# print(n.show())


preorder = [3,1,2,4]
inorder = [1,2,3,4]
n = Solution().buildTree(preorder,inorder)
