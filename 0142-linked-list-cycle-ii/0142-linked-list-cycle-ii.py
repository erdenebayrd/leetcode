# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time: O(N)
        # space: O(1)
        # method: Floyd's cycle find algo

        firstMeetPoint = None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                firstMeetPoint = slow
                break
        if firstMeetPoint is None: # meaning no cycle
            return None
        fast = head
        slow = firstMeetPoint
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow