# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isIdentical(p,q):
            if p is None and q is None:
                return True
            
            if p is None or q is None:
                return False
            
            return q.val == p.val and isIdentical(q.left, p.left) and isIdentical(q.right, p.right)

        if root is None and subRoot is not None: 
            return False
        
        if root is None and subRoot is None:
            return True
        
        if isIdentical(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


