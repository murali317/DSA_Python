# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # time - O(n) each node is visited exactly once.
        # space - O(w) where w = max width of the tree & W.C - O(n) for complete tree, B.C - O(1) for skewed tree. could be said as O(n) (simplified to O(n))
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue: # for loop run only once as queue starts with 1 element (root)
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
        
        # -------------- RECURSION --------------------
        # INTUITION - You're swapping the left and right subtrees of every node in a bottom-up manner (because the recursion goes all the way down before swapping happens on the way back up).
        # time - O(n) each node is visited exactly once to make a recursive call on left, on right and swap them.
        # space - O(h) # depends on height(h) of the tree, due to recursive call stack & B.C is O(log n) for balanced tree, W.C is O(n) in skewed tree where (h = n)

        if not root: # i.e., we've reached the bottom of the tree
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root