# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trees(self, start, end):
        if start > end:
            return [None]

        tree = []
        for i in range(start, end + 1):
            left = self.trees(start, i - 1)
            right = self.trees(i + 1, end)

            for l in left:
                for r in right:
                    tree.append(TreeNode(i, l, r))

        return tree

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        return self.trees(1, n)
