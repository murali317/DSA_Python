# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time - O(n) - single-pass traversal, each node is visited once.
        # space - O(1) - In-place modification, no auxiliary space required.
        
        a = head
        if a is not None: # first check if a is None or not
            while a.next is not None: # (while a and a.next:) is better than having both (if and while)
                if a.val == a.next.val:
                    a.next = a.next.next
                else:
                    a = a.next
        return head