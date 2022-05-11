from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        from_left = True
        output, stack = [], [root]

        while len(stack) > 0:
            n = len(stack)
            values = []

            for _ in range(n):
                if from_left:
                    node = stack.pop(0)
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                else:
                    node = stack.pop()
                    if node.right:
                        stack.insert(0, node.right)
                    if node.left:
                        stack.insert(0, node.left)
                values.append(node.val)

            from_left = not from_left
            output.append(values)

        return output
