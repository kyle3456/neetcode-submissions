# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root = TreeNode(val)
            return root
        def move(prev, direction, curr):
            if curr is None:
                if direction == "L":
                    prev.left = TreeNode(val)
                else:
                    prev.right = TreeNode(val)
                return

            if curr.val < val:
                move(curr, "R", curr.right)
            else:
                move(curr, "L", curr.left)

        move(root, None, root)
        return root