# 110. Balanced Binary Tree


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def height(root):
            nonlocal balanced
            if not root:
                return 0

            l = height(root.left)
            if not balanced:
                return 0
            r = height(root.right)

            if abs(l - r) > 1:
                balanced = False
                return 0

            return 1 + max(l, r)

        height(root)

        return balanced



