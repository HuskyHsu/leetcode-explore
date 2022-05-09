from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_value = float("-inf")

    def max_path(self, node) -> int:
        if node is None:
            return 0

        left_max = max(self.max_path(node.left), 0)
        right_max = max(self.max_path(node.right), 0)

        self.max_value = max(self.max_value, node.val + left_max + right_max)

        return node.val + max(left_max, right_max)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path(root)
        return self.max_value
