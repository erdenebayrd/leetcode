# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        left -= 1
        right -= 1
        arr[left:right + 1] = arr[left:right + 1][::-1]
        head = ListNode()
        currentHead = head
        for i in range(len(arr)):
            currentHead.next = ListNode(arr[i])
            currentHead = currentHead.next
        del arr
        return head.next