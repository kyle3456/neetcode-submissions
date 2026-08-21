# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        d = []
        def dfs(root):
            if root is None:
                return
            
            dfs(root.left)
            d.append(root.val)
            dfs(root.right)

        dfs(root)
        return d[k - 1]
            