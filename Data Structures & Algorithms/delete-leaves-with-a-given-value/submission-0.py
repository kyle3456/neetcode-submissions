# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if node == None:
                return False
            if node.val == target and node.left == None and node.right == None:
                return True
            l = dfs(node.left)
            if l:
                node.left = None
                if node.val == target and node.right == None:
                    return True
            r = dfs(node.right)
            if r:
                node.right = None
                if node.val == target and node.left == None:
                    return True
            return False
        node = root
        curr = dfs(node)
        if curr:
            return None
        return node

            