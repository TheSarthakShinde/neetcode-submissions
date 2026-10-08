# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans =[]
        que = deque([root])
        while que:
            level = []
            size = len(que)
            for _ in range(size):
                e = que.popleft()
                level.append(e.val)
                if e.left:
                    que.append(e.left)
                if e.right:
                    que.append(e.right)
            ans.append(level)
        return ans



        