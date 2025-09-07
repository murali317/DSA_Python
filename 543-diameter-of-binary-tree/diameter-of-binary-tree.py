# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # INTUITION - for every node - longest path is left subtree depth + right subtree depth and We want to find max (left depth + right depth) across all nodes which will come through recursion. Then finally return the stored maximum diameter (dia).

        # time - O(n) as it is DFS that touches every node exactly once.
        # space - O(h) - O(log n) for balanced & O(n) for skewed (worst case)
        self.dia = 0
        def depth(root): # root will be each node at each step covering all nodes
            if not root:
                return 0
            node = root
            left_depth = depth(node.left) # left depth of each node recursively
            right_depth = depth(node.right) # right depth of each node recursively
            self.dia = max(self.dia, left_depth + right_depth)  # a player that explores the tree and keeps updating the score
            return 1 + max(left_depth, right_depth) # Because you're moving one level up (the current node itself) plus the deeper of the two children. (think going above from bottom). Finally depth() returns the depth of current node to its parent.
        depth(root)
        
        return self.dia # We return self.dia after the entire traversal is complete, because only then we know the maximum diameter.