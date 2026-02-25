# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # INTUITION - Using queue to apply BFS
        # time - O(n) space - O(w) - O(n) WC, O(log n) BC where w is width of the tree
        
        # if not root:
        #     return 0
        # c = 0
        # queue = deque()
        # queue.append(root)
        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     c += 1 # here we are counting the levels.
        # return c # root = [3,9,20,null,null,15,7] Output: 3

        # RECURSIVE APPROACH
        # time - O(n)
        # space - O(h) as it winds up from the bottom, we consider height & logn for balanced, n for skewed.
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)

        # for height at each node = 1+max(height of lst, height of rst)