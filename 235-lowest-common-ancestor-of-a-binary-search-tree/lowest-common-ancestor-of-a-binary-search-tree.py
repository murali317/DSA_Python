# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # ------- WITHOUT USING BST PROPERTIES ----------
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right

        # ------- USING BST PROPERTIES ----------
        # ------------ RECURSION ---------------
        # INTUITION - ✅ 3 Core Conditions:
        # If both p and q are less than root → LCA lies in left subtree
        # ➤ Recur on root.left
        # If both p and q are greater than root → LCA lies in right subtree
        # ➤ Recur on root.right
        # If p <= root <= q or q <= root <= p → this root is the split point, hence the LCA

        # time - O(h) - Every recursive step or decision narrows the search to one subtree only (left or right). That’s because BST properties allow us to eliminate half of the tree based on values.
        # space - O(h)
        if not root:
            return None
        if root == p or root == q:
            return root
        if p.val < root.val and q.val > root.val:
            return root
        if p.val > root.val and q.val < root.val:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q) # dont forget to return
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q) # dont only compute, also return 

        # ------------------- ITERATIVE ------------------
        # 
        # time - O(h) # log n for balanced (B.C), n for skewed (W.C)
        # space - O(1)
        
        while root:
            if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
                return root
            if (p.val < root.val and q.val < root.val):
                root = root.left
            elif (p.val > root.val and q.val > root.val): # if 'if' is used, may lead to TLE
                root = root.right
            else: # elif p.val == root.val or q.val == root.val
                return root
        return None # if no root found
            
            