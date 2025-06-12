# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # time - O(n) space - O(n)
        # traversal = []  
        # if not root:
        #     return [] 
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        # METHOD - II ---------------------
        # no need of storing into left, right if there would be a global var (traversal)
        def inorder(root):
            if not root:
                return []
            left = inorder(root.left) 
            traversal = [root.val]
            right = inorder(root.right)
            return left + traversal + right
        return inorder(root)

        #  ------------ ITERATIVE APPROACH ------------
        # time - O(n) pushed & popped once for n nodes.
        # space - O(h) where h = height of the tree, B.C. - balanced tree(O(log n)) W.C. - skewed tree (O(n))
        # curr = root; res = []; stack = []
        # while stack or curr:
        #     if curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     else:
        #         curr = stack.pop()
        #         res.append(curr.val) # popping from bottom - top
        #         curr = curr.right
        # return res