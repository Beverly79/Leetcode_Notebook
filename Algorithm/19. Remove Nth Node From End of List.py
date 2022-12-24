# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast_node = head # both ListNode
        slow_node = head
        for i in range(n):
            fast_node = fast_node.next # move to the next ListNode
            # this loop will stop when the fast when slow is n step behind fast
        
        if not fast_node: 
            # if fast_node is already None
            # which means we should delete the first one
            # we return the second node
            return head.next
        
        while fast_node.next: # while fast is not the last node
            fast_node = fast_node.next
            slow_node = slow_node.next
        next_node = slow_node.next
        slow_node.next = next_node.next
        return head



'''
Note:
Two pointers needed.
In order to go through the linked list only once,
we need two pointers to keep the distance as n,
to let us know which node is the nth from the end.

Edge case:
Deleting the first node (head)
'''

