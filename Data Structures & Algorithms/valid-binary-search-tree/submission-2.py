# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == []:
            return True
        
        if root is None:
            return True

        def MinMax(root):
            nonlocal mi
            nonlocal ma

            if root.val < mi:
                mi = root.val
            if root.val > ma:
                ma = root.val
            
            if root.left:
                MinMax(root.left)
            if root.right:
                MinMax(root.right)
            
            return [mi, ma]
        
        if root.left:
            mi = 99999999
            ma = -99999999
            s = MinMax(root.left)
            if root.val <= s[1]:
                return False
            
        if root.right:
            mi = 99999999
            ma = -99999999
            s = MinMax(root.right)
            if root.val >= s[0]:
                return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)
        
        
                