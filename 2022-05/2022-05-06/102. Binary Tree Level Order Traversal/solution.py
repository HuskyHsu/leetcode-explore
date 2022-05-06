from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        stack = [root]
        output = []

        while len(stack) > 0:
            values = []
            n = len(stack)

            for _ in range(n):
                node = stack.pop(0)
                values.append(node.val)

                if node.left:
                    stack.append(node.left)

                if node.right:
                    stack.append(node.right)

            output.append(values)

        return output
