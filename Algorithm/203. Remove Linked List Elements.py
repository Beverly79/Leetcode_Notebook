# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = dummy = ListNode(val=None, next=head)
        while cur.next: # stops in the end of the list
            if cur.next.val == val: # the case we wanna delete the next node
                cur.next = cur.next.next # delete the next node
            else: # do not delete
                cur = cur.next # move on
            # if we wanna delete the last node,
            # cur.next.next is None, after deletion, cur.next is None,
            # while loop stops
        return dummy.next # which is the head