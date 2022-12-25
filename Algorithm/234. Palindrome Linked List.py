# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        l = []
        # put every node into l
        while cur:
            l.append(cur)
            cur = cur.next
        l = l[::-1] # reverse l
        cur = head
        for i in l:
            if i.val != cur.val:
                return False
            cur = cur.next
        return True
        
