# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # time: O(N)
        # space: O(1)
        # method: reversed first half
        """
        at first we need to count how many nodes in this linked list
        lets call it "count"
            1. we need to find secondHalfHead pointer by counting nodes from head to (n - n // 2 + 1)
            2. firstHalfHead which will be n//2 'th node
            3. reverse first half (first n // 2 nodes)
            4. compare first half head and second half head till those pointer is null
        """
        size = 0
        current = head
        while current:
            size += 1
            current = current.next 
        if size == 1:
            return True
            
        secondHalfHead = None
        current = head
        secondHalfStartedFrom = size - size // 2 + 1
        currentNodeNumber = 1
        while current:
            if currentNodeNumber == secondHalfStartedFrom:
                secondHalfHead = current
                break
            current = current.next
            currentNodeNumber += 1
        
        # reverse first half
        firstHalfEndAt = size // 2
        
        current = head
        prev = None
        firstHalfHead = None

        currentNodeNumber = 1
        while currentNodeNumber != firstHalfEndAt:
            if prev is None:
                prev = current
                current = current.next
                nextNode = current.next
                current.next = prev
                prev.next = None
                prev = current
                current = nextNode
            else:
                nextNode = current.next
                current.next = prev
                prev = current
                current = nextNode
            currentNodeNumber += 1
        firstHalfHead = prev
        if firstHalfEndAt == 1:
            firstHalfHead = head
        while firstHalfHead is not None and secondHalfHead is not None:
            # print(firstHalfHead.val, secondHalfHead.val)
            if firstHalfHead.val != secondHalfHead.val:
                return False
            firstHalfHead = firstHalfHead.next
            secondHalfHead = secondHalfHead.next
        return True