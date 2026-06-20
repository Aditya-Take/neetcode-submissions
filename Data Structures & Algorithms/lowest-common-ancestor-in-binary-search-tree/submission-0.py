# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lca = root

        def ans(root):
            if root is None:
                return
            
            if p.val > root.val and q.val > root.val:
                ans(root.right)
            elif p.val < root.val and q.val < root.val:
                ans(root.left)
            else:
                self.lca = root
        ans(root)

        return self.lca