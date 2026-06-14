# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # time: O(N)
        # space: O(1)
        # method: Tortoise and Hare algo (Floyd Cycle detection by slow and fast pointer) reverse linked list (only last half)
        prev = None
        slow = fast = head
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        tail_end = prev

        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        current_head = head
        tail = prev
        result = tail.val + current_head.val
        while tail != tail_end:
            current_head = current_head.next
            tail = tail.next
            result = max(result, tail.val + current_head.val)
        return result