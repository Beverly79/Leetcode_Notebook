# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

########### Time O(n + m + max(n,m))  Space O(1) ###########
class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        n1 = 0
        n2 = 0
        count1 = 0
        count2 = 0
        # convert the two linked list in to integers
        while cur1:
            n1 += cur1.val * pow(10,count1)
            cur1 = cur1.next
            count1 += 1
        while cur2:
            n2 += cur2.val * pow(10,count2)
            cur2 = cur2.next
            count2 += 1
        n = n1 + n2

        if n == 0:
            return ListNode()

        cur = head = ListNode()
        while n >= 10: # convert integers into linked list
            cur.val = n % 10
            cur.next = ListNode()
            cur = cur.next
            n = n // 10
        cur.val = n
        
        return head


########### Time O(max(n,m))  Space O(1) ###########
class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = head = ListNode()
        cur1 = l1
        cur2 = l2
        n = 0
        e = 0
        while cur1 or cur2:
            n = e
            if cur1: # the value from list1
                n += cur1.val
                cur1 = cur1.next
                
            if cur2:
                n += cur2.val # the value from list 2
                cur2 = cur2.next
                
            cur.next = ListNode(n%10) # make sure the total of the values is smaller than 10
            e = n//10 # e is either 0 or 1
            cur = cur.next

        if e == 1: # add one more node to the end (one more digit)
            cur.next = ListNode(1)
        return head.next