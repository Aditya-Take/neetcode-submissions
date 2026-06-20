# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same_tree(p,q):
            if p is None and q is None:
                return True
            
            if (p and not q) or (q and not p):
                return False
            
            if p.val != q.val:
                return False
            
            return same_tree(p.left,q.left) and same_tree(p.right,q.right)
        
        def compare(root, subRoot):
            if root is None:
                return False
            
            if same_tree(root,subRoot):
                return True
            
            return compare(root.left,subRoot) or compare(root.right,subRoot)

        return compare(root,subRoot)