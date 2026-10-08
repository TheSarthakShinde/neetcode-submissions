# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def solve(node):
            if not node:
                return 0

            lh = solve(node.left)
            rh = solve(node.right)
            if abs(lh - rh) > 1:
                self.balanced = False
            return 1 + max(lh,rh)
        self.balanced = True
        solve(root)
        return self.balanced
             
            
        