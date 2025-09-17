# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # ---- Includes 'null' to preserve structure -----

        # time - O(n) 
        # space - O(n)
        if not root:
            return ''
        s = ''
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                s += str(node.val) + ','
                queue.append(node.left)
                queue.append(node.right)
            else:
                s += 'null,'
        return s[:-1:] # or s.rstrip(',') - to remove last appended extra ','
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # -------------- Uses index + queue to reconstruct tree ------
        # time - O(n)
        # space - O(n)
        if not data:
            return None            
        vals = data.split(',') # ['1', '2', '3', 'null', 'null', '4', '5']
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        i = 1 # start from 1st index as root is at 0
        while queue:
            # assign left child
            node = queue.popleft()
            if vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1 # this is to check twice(left & right) at a time
            # assign left child
            if vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))