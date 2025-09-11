# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # time - O(n)
        # space - O(h) - due to recursion stack (O(log n) for balanced, O(n) for unbalanced)
        def dfs(root, c):
            if not root:
                return False
            c += root.val # Always add to current_sum rather than overwriting it by c = ...
            left = dfs(root.left, c) # assigning it to root.left changes(overwrites) the structure of the tree, instead we just want to traverse it and count the vals. That means left here was assigned True or False values from the dfs fxn.
            right = dfs(root.right, c) # same with right also
            if not root.left and not root.right: # only check at leaf nodes.
                return c == targetSum
            return left or right # will return True if either left or right has True otherwise False - Without this line, the recursive calls would evaluate, but you'd lose the result of those evaluations and always return None or nothing — which would break the logic. So finally this line means If either subtree has a valid path, return True
        return dfs(root, 0)