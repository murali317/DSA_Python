# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # INTUITION - observe that we have to return the node (index not needed). First check if there exists a cycle. If yes, MOVE SLOW TO HEAD, NOW MOVE BOTH SLOW & FAST UNTIL THEY MEET. RETURN SLOW WHERE THEY MEET.
        # time - O(n) -> [since O(n) + O(n) = O(2n) = O(n)]
        # space - O(1) -> using two pointers: slow and fast & no extra space used regardless of list size.

        slow = head
        fast = head
        while fast and fast.next: # O(n)
            slow = slow.next
            fast = fast.next.next # first checking whether there exists a cycle or not
            if slow == fast:
            # Phase 2: Find the start of the cycle
                slow = head  # Move slow pointer to the head of the list
                while slow != fast: # O(n) # Move both slow and fast one step at a time until they meet
                    slow = slow.next
                    fast = fast.next
                return slow  # The node where the cycle begins
        return None # observe "Optional[ListNode]" - meaning the function can return either a ListNode (if there's a cycle) or None (if there's no cycle).