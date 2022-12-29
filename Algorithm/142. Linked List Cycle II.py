# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


########### Time O(n)  Space O(n) ###########
class Solution1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        cur = head
        while cur:
            if cur in s:
                return cur
            else:
                s.add(cur)
                cur = cur.next
        return None


########### Time O(n)  Space O(1) ###########
class Solution2:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: # they meet
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow


        return None