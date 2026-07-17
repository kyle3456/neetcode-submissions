# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 1
        stack = [(root)]


        def findBigger(node):
            nonlocal res
            temp = 0
            if node.left and node.left.val >= stack[-1].val:
                res += 1
                temp += 1
                stack.append(node.left)
            
            if node.left:
                findBigger(node.left)
            
            if temp == 1:
                temp = 0
                stack.pop()
            
            if node.right and node.right.val >= stack[-1].val:
                stack.append(node.right)
                res += 1
                temp += 1
            
            if node.right:
                findBigger(node.right)

            if temp == 1:
                stack.pop()
        
        findBigger(root)
        return res
            
            