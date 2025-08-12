# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # time - O(n) # here it is O(right) but if left, right = 1, n -> it would be O(n)
        # space - O(1) # all are constant pointers (in-place reversal).

        if not head or left == right:
            return head
        
        # Step-1: Reach node at position 'left'
        dummy = ListNode(0, head) # a dummy node pointing to head.
        leftPrev, cur = dummy, head
        for _ in range(left - 1): # O(left - 1)
            leftPrev, cur = cur, cur.next

        # now, cur = 'left' & leftPrev = 'node before left'
        # Step-2: Reverse from left -> right
        prev = None
        for _ in range(right - left + 1): # O(right - left + 1)
            tempNext = cur.next
            cur.next = prev
            prev, cur = cur, tempNext
        
        # update pointers
        leftPrev.next.next = cur # cur is node after 'right'
        leftPrev.next = prev # prev is 'right'
        return dummy.next
            