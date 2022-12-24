# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head: # when list has at least one value
            curr = head
            while curr.next: # stops at the last node
                if curr.val == curr.next.val: # next has the same value
                    curr.next = curr.next.next
                else:
                    curr = curr.next
        return head