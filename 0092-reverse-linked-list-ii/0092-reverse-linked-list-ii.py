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
        middleIndex = (left + right) // 2 # 5, 6, 7, 8 => (5 + 8) // 2 = 13 // 2 = 6
        for i in range(left, right + 1, 1):
            if i > middleIndex:
                break
            # swap arr[i], arr[right - i + left]
            tmp = arr[right - i + left]
            arr[right - i + left] = arr[i]
            arr[i] = tmp
        # print(arr)
        head = ListNode()
        currentHead = head
        for i in range(len(arr)):
            currentHead.next = ListNode(arr[i])
            currentHead = currentHead.next
        return head.next