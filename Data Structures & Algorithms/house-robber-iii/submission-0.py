# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node is None:
                return (0,0)
            l_skip, l_rob = dfs(node.left)
            r_skip, r_rob = dfs(node.right)

            rob = l_skip + r_skip + node.val
            skip = max(l_rob, l_skip) + max(r_rob, r_skip)
            return (skip, rob)

        return max(dfs(root))
