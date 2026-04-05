# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        # Step 1: Create dummy node
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 2: Move prev to (left-1)
        for _ in range(left - 1):
            prev = prev.next

        # Step 3: Reverse
        curr = prev.next

        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next