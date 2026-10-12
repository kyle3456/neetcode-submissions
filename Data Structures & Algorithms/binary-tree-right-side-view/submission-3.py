# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        s = [True] * 101
        res = []
        def check(node, layer):
            if not node:
                return
                
            if s[layer]:
                s[layer] = False
                res.append(node.val)

            if node.right:
                check(node.right, layer + 1)
            if node.left:
                check(node.left, layer + 1)
            return

        check(root, 0)
        return res



            