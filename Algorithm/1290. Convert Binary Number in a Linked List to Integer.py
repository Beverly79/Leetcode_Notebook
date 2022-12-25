# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        cur = head
        while cur:
            num *= 2
            num += cur.val
            cur = cur.next
        return num