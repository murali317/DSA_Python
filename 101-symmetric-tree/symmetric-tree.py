# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    # INTUITION - symmetric means we have to check if root.left.val == root.right.val, left.left.val == right.right.val and left.right == right.left So need to take a recursive fxn to check all the nodes in both left and right sub trees.
    # time - O(n) You visit every node in the binary tree once to compare its mirror position.
    # space - O(h)

        if not root:
            return True
        return self.helper(root.left, root.right) # calling helper fxn here in main fxn

    def helper(self, left, right): # check left & right subtrees
        if not left and not right: #if both left & right subtrees / if no children, symmetric
            return True
        if not left or not right: # any one of the children is not there, not symmetric
            return False
        if left.val != right.val: # if different values, not symmetric
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)