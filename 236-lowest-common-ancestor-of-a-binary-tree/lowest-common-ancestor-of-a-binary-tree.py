# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # INTUITION - first check if the root itself = p or q, if not, go traverse recursively to left & right subtrees, if they return root(/val) (not return None), then it could be the LCA. (It is allowed that a node to be a descendant of itself).
        # time - O(n)
        # space - O(h) # as it signifies height of the tree and recursion stack space=O(h)
        if not root:
            return None
        if root == p or root == q: # if root itself is p or q, then root is LCA
            return root
        left = self.lowestCommonAncestor(root.left, p, q) # traverse to left subtree
        right = self.lowestCommonAncestor(root.right, p, q) # traverse to right subtree
        if left and right:
            return root
        return left if left else right 
