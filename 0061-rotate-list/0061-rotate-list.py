# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # time: O(N)
        # space: O(1)
        # method: linked list
        if not head:
            return None
        n = 0
        current = head
        while current:
            current = current.next
            n += 1
        k %= n
        if k == 0:
            return head

        current = head
        for _ in range(n - k - 1):
            current = current.next
        newTail = current
        
        tail = None
        while current:
            tail = current
            current = current.next
        
        tail.next = head
        head = newTail.next
        newTail.next = None
        return head
            