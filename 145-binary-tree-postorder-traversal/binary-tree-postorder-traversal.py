# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # time - O(n) You visit every node once.
        # space - O(n) or O(h) varies for best/average(balanced) & worst case(skewed)
        res = []
        def postorder(root):
            if not root:
                return []
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return res

        # ------- ITERATIVE APPROACH ------------
        # time - O(n) each node is pushed & popped once
        # space - O(h)
        stack = []
        res = []; curr = root; prev = None
        while stack or curr:
            if curr: # Keep going left, pushing nodes.
                stack.append(curr)
                curr = curr.left
            else:
                temp = stack[-1] # Look at the top node in the stack (peek)
                # check if right subtree exists & if isn't visited yet ➔ move right.
                # This ensures you only process the root after both left and right are done.
                if temp.right and prev != temp.right: # prev tracks what was just visited, so you don't re-visit it.
                    curr = temp.right
                # No right or already visited ➔ now visit the node and pop.
                else:
                    res.append(temp.val)
                    prev = stack.pop()
        return res
        