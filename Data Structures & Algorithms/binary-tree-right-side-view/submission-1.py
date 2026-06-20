# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            lvl = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                lvl.append(node.val)
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(lvl[-1])
        
        return ans
