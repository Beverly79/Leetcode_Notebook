# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if head.next == None:
            return head
        mark = None
        cur =  dummy = ListNode(val=200,next=head)
        while cur.next.next: # cur is at least last 3rd
            if cur.next.val == cur.next.next.val: # same value mark
                mark = cur.next.val
            if cur.next.val == mark:
                cur.next = cur.next.next
            else:
                cur = cur.next
        if cur.next.val == mark:
            cur.next = None
        return dummy.next