# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        value = []
        while cur:
            value.append(cur.val) # add all the value into a list
            cur = cur.next
        value = value[::-1] # reverse the list
        cur = head
        for i in range(len(value)-1):
            cur.val = value[i]
            cur.next.val = value[i+1]
            cur = cur.next
        return  head
