# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or head.next == None:
            return head

        start = end = dummy = ListNode(next=head)
        for i in range(left-1):
            start = start.next 
            end = end.next
        # start is the last node of the first part the the linked list
        l = []
        for i in range(right-left+1):
            end = end.next
            l.append(end.val)
        end = end.next # end is the beginning of the rest of the linked list
        l = l[::-1] # reverse
        
        for i in l:
            start.next = ListNode(i)
            start = start.next
        start.next = end

        return dummy.next
