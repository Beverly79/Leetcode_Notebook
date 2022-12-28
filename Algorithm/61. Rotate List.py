# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head

        cur = head
        l = []
        while cur:
            l.append(cur)
            cur = cur.next
        diff = k % len(l) # k mode length to set the difference of two pointers

        # two pointers, len = l
        # slow: idx{0} -> idx{l-diff}
        # fast: idx{diff} -> None(idx{l})
        slow = head
        fast = head
        for i in range(diff):
            fast = fast.next
        
        while fast.next: # stops when fast is the last one and slow is l-k
            slow = slow.next 
            fast = fast.next
        fast.next = head # add the old head to the end
        head = slow.next # slow.next is the new head
        slow.next = None # slow is the new end
        return head
