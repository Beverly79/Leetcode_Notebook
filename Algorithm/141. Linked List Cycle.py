# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


########### Time O(n)  Space O(n) ###########
class Solution1: 
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        node_list = []
        while curr: # stops at the last node if it's not a cycle
            if curr not in node_list:
                node_list.append(curr)
                curr = curr.next
            else:
                return True
        return False


########### Time O(n)  Space O(1) ###########
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # if fast travel speed is twice slow travel speed,
        # they will meet within two circles.
        while fast and fast.next: # stops when fast is the last one or the last two
            slow = slow.next # slow move to next
            fast = fast.next.next # fast move two steps
            if slow == fast:
                return True
        # if they never meet before the while loop stops (fast goes to end)
        # it's not a circle
        return False


########### Time O(n)  Space O(1) ###########
class Solution3:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        while curr: # stops when it goes to the end
            curr.val = None # change the value of the node into None to mark it
            curr = curr.next
            if curr: # only mark it when it's not the last one
                if curr.val == None: # if it is marked
                    return True
        return False