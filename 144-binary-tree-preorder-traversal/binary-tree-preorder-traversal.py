# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # time - O(n) we visit each node(root, left, right) once
        # space - O(n) for res & callstack
        # res = []
        # def preorder(root):
        #     if not root: # base case
        #         return [] # that means go one step back to 2 & call 5, goes to 6, no 6.left -> that means go back to 5 & call 7, then back to 1 & call 3....
        #     res.append(root.val)
        #     preorder(root.left)
        #     preorder(root.right)
        # preorder(root)
        # return res

        # ---------- ITERATIVE METHOD ----------
        # time - O(n) # every node is visited only once.
        # space - O(h) h is height of the tree. W.C is if O(n) for a skewed tree (like LL)
        curr, stack, res = root, [], [] # stack is for right subtrees to visit later
        while stack or curr:
            if curr:
                res.append(curr.val)
                stack.append(curr) # push right subtree to visit it later
                curr = curr.left # Now This dives deeper down the left side, like a recursive call would until left is found.
            else:
                curr = stack.pop() # If curr is None (you've hit the end of a left path), you pop from the stack. Now you set curr to that right child, and the loop continues to process it just like before.
                curr = curr.right
        return res
