# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # using reverse post order
        def revpost(node,level,ans):
            if not node:return 
            if len(ans) == level:
                ans.append(node.val)
            if node.right:
                revpost(node.right,level+1,ans)
            if node.left:
                revpost(node.left,level+1,ans)
        ans = []
        revpost(root,0,ans)
        return ans
        