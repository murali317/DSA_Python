# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # INTUITION - JUST REMEMBER TO APPLY BST PROPERTIES

        # time - O(h) # see recursive approach for explanation.
        # space - O(1) uses constant space since it's iterative (no recursion or stack space used).
        curr = root
        if not root:
            return TreeNode(val)
        while curr:
            if val < curr.val:
                if curr.left == None:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            elif val > curr.val:
                if curr.right == None:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right
        return root


        # ------------ RECURSION --------------------
        # time - O(h) - unlike normal DFS, there's no need to go both to left and right, as of BST property, if val<root, we go only to left and right in opposite case. That's it only one side and That’s equal to the height of the path you took. so height is also same - it is defined as longest distance from root - a leaf. At each step, you eliminate half the tree (like binary search). Max number of steps = height of the tree = h
        # space - O(h)
        if not root: # if root is None
            return TreeNode(val) # this is where the insertion happens.
            # The recursive return connects the new node back into its correct place.
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root # as asked in the question