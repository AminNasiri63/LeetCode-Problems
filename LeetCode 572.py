# 572. Subtree of Another Tree


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isTheSame(p, q):
            if not p and not q:
                return True

            if (p and not q) or (q and not p):
                return False

            if p.val != q.val:
                return False

            return isTheSame(p.left, q.left) and isTheSame(p.right, q.right)

        def hasSub(root):
            if not root:
                return False

            if isTheSame(root, subRoot):
                return True

            return hasSub(root.left) or hasSub(root.right)

        return hasSub(root)


