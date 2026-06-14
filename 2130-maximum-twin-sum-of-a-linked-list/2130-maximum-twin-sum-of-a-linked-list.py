# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # time: O(N)
        # space: O(1)
        # method: reverse linked list (only last half)
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1
        
        count = 0
        size >>= 1
        prev = None
        curr = head
        while curr:
            if count >= size:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            else:
                prev = curr
                curr = curr.next
                count += 1

        tail = prev
        
        curr_head = head
        curr_tail = tail
        result = head.val + tail.val
        while size:
            size -= 1
            result = max(curr_head.val + curr_tail.val, result)
            curr_head = curr_head.next
            curr_tail = curr_tail.next
        return result
