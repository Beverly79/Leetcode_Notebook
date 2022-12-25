# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers: fast and slow
        fast = head
        slow = head
        while fast.next: # stops when fast goes to the last node
            if fast.next.next == None: # if fast is the last 2nd
                return slow.next
            else:
                fast = fast.next.next
                slow = slow.next
        return slow