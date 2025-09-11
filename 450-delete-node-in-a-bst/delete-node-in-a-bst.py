# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:        
        # INTUITION - first search for that particular key then apply the 3 base cases.
        # time - O(h) We may have to traverse from the root down to a leaf node to find the key node which signifies nothing but the height of the tree.
        # space - O(h) Recursive stack space
        if not root:
            return None
        # curr = root
        # while curr: # there's no need to loop manually, recursion handles the traversal
        if key < root.val:
            root.left = self.deleteNode(root.left, key) # reassigning the updated version of left subtree (after deleting/not deleting have to give back to root.left)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # this means root.val == key

             # Case 1: No children - just remove that node from the tree
            if not root.left and not root.right:
                return None # remove the whole node as there's no children to replace with
                # this return None goes back to its parent call and get assigned to root.left = None or root.right = None (means deleting that node, which is a child to parent). I mean set that child pointer to None means deleting only. "Recursion in trees isn’t just “doing work” — it’s rebuilding the tree from the bottom up using return values."

            # Case 2: One child - This tells the parent to directly connect to the (left/right) child, bypassing the deleted node.
            elif not root.right:
                return root.left # return the left child to parent after deleting root
            elif not root.left:
                return root.right # return the right child to parent after deleting root
                # return None - would remove the whole node & its child

            # Case 3: Two children - find inorder successor & replace the node with this.
            successor = self.helper(root.right) # finding smallest node in the right subtree.
            root.val = successor.val # replacing the node with the found node ⬆️.
            root.right = self.deleteNode(root.right, successor.val) # Now we delete the duplicate node (the inorder successor) from the right subtree and reassign the updated right subtree by recursively deleting it.
        return root

    def helper(self, node):
        while node.left:
            node = node.left
        return node
