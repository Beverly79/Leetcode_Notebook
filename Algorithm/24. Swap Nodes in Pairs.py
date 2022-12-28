# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        cur = head
        while cur.next: # stops when there's no more than one node (nothing to swap)
            temp = cur.val # store the value of the next node
            cur.val = cur.next.val # swap
            cur.next.val = temp
            cur = cur.next.next 
            if cur == None: # if it reaches the end of the linked list
                return head
        return head