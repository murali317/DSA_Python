# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # INTUITION - take 3 pointers (prev, a, next_node). assign them to None, head, a.next. Move prev, a and next_node until a is None and return prev.
    # time - O(n) - each node is visited once in a single pass.
    # space - O(1) - no extra space except few pointers and in-place reversal this is.
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        a = head  # Start with the head of the list
        while a is not None:
            next_node = a.next  # Save the next node
            a.next = prev  # Reverse the link
            prev = a  # Move `prev` forward
            a = next_node  # Move `a` forward
        return prev # `prev` will be the new head of the reversed list
        