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

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []
        n = root
        self.__stack_left(root)
    
    def __stack_left(self, n:TreeNode) -> None:
        while n:
            self.stack.append(n)
            n = n.left
        return

    def next(self) -> int:
        n = self.stack.pop()
        val = n.val
        if n.right:
            self.__stack_left(n.right)
        return val
    
    def print(self):
        print('stack:'+' '.join([str(n) for n in self.stack]))

    def hasNext(self) -> bool:
        return len(self.stack) > 0
    
root = TreeNode(7,TreeNode(3),TreeNode(15,TreeNode(9),TreeNode(20)))
print(root.show())
iter = BSTIterator(root)

iter.print()
while iter.hasNext():
    print(iter.next())