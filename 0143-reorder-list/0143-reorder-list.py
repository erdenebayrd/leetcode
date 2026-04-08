# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1 -> 2 -> 3 -> 4
        # 1 -> 2 -> 3 <- 4
        # 1 -> 4 -> 2 -> 3 -> None

        # 1 -> 2 -> 3 -> 4 -> 5
        # 1 -> 2 -> 3 <- 4 <- 5
        # 1 -> 5 -> 2 -> 4 -> 3
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        current = slow
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        
        # 1 -> 2 -> 3 <- 4
        #      ^    ^
        # 1 -> 4 -> 2 -> 3

        """
        1 -> 2 -> 3 -> 4 -> 5
        
        1 -> 2 -> 3 <- 4 <- 5
                  ^^
        1 -> 5 -> 2 -> 4 -> 3
        """
        right = prev
        left = head
        while left.next and right.next:
            leftNext = left.next
            rightNext = right.next
            left.next = right
            right.next = leftNext
            left = leftNext
            right = rightNext