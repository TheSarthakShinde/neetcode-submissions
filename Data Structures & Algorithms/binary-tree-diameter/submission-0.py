# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self,node):
        if not node:
            return 0
        lh = self.solve(node.left)
        rh = self.solve(node.right)
        self.diameter = max(self.diameter, lh+rh)
        return 1 + max(lh,rh)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.solve(root)
        return self.diameter
        