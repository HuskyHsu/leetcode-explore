from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Error(Exception):
    pass


class Solution:
    def depth(self, node) -> int:
        if node is None:
            return 0

        depth_left = self.depth(node.left)
        depth_right = self.depth(node.right)

        if abs(depth_left - depth_right) > 1:
            raise Error

        return 1 + max(depth_left, depth_right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        try:
            self.depth(root)
            return True
        except Error:
            return False
