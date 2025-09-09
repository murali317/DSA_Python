from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # INTUITION - have to take a for loop to loop through each level (containing left & rights), take an inner (sublist) to append those left & rights each time to complete that particular level, then same continues for next levels.
        # time - O(n)
        # space - O(n)
        queue = deque()
        ans = []
        queue.append(root) # initially queue will store the root.
        if not root:
            return []
        while queue:
            inner = [] # inner sub list that gets emptied after every iteration.
            for i in range(len(queue)):
                node = queue.popleft() # popping the left most element i.e., root node
                inner.append(node.val)
                if node.left: # checking is left exists to only append that node.
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(inner) # appending each sub list to ans after every iteration.
        return ans

        # Recursion is very inefficient (time - O(n^2)) so dont prioritize it.