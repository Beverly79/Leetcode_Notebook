# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        while cur:
            for i in range(m-1):
                if cur.next == None: # if cur is the last one
                    return head
                cur = cur.next # keep m (move m-1 step to mth node)

            for j in range(n):
                if cur.next == None: # if cur is the last one, nothing to delete
                    return head
                cur.next = cur.next.next # delete the next one
            cur = cur.next
        return head