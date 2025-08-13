# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # INTUITION - just have 2 pointers (slow, fast). while iterating, if slow == fast, there exists a cycle.
        # time - O(N) #  In the worst case, fast will traverse all nodes before detecting a cycle.
        # space - O(1)

        slow = head
        fast = head
        while fast and fast.next: # we had to use these two, bcoz of using fast.next.next (i.e, fast.next.next can raise an error if fast.next is None)
            slow = slow.next
            fast = fast.next.next 
            if slow == fast: # if this is met, then cycle exists.
                return True
        return False # if we give this in else condition, the loop will terminate in the first iteration itself.
        # so if we give here, it returns false only after traversing all nodes and get no cycle.
