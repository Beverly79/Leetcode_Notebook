# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


########### Time O(n)  Space O(n) ###########
class Solution1:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        l = []
        while cur:
            l.append(cur)
            cur = cur.next
        l  = l[::-1] # reverse
        l[len(l)//2].next = None # delete the later half
        l = l[:len(l)//2] # the later half nodes

        cur = head
        for node in l:
            cur.next = ListNode(val=node.val, next=cur.next)
            if cur.next:
                cur = cur.next.next
            else:
                break


########### Time O(n)  Space O(1) ###########
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next != None and head.next.next != None: # at least three nodes
            mid = head
            tail = head
            pre = head
            while tail.next:
                tail = tail.next
                if tail.next != None:
                    tail = tail.next
                    pre = mid
                    mid = mid.next
            # mid is the middle one
            # pre is the node before mid
            # tail is the last one
            # should reverse from mid.next to end
            # two cases:
            # [n0,n1,n2] -> mid:n1, tail:n2, pre:n0
            # [n0,n1,n2,n3] -> mid:n1, tail:n3, pre:n0
            
            mid = mid.next
            pre = pre.next
            part2 = mid # first node of part2
            pre.next = None # truncate everything after mid
            # in order to reverse part2
            # we go through part2 and use a temp to store the next node
            pre = None # pre is None and after reverse it will be the end
            # example: reverse[3, 4]

            while part2:
                temp = part2.next # store the next node in temp (4)
                part2.next = pre # add the former node as the next (None)
                pre = part2 # former node move to the current node (3)
                part2 = temp # current node move to the temp (4)
            # pre will be the last node in the origin list
            # and also the first one after the reverse
            
            # now we combine part1 and part2
            part1 = head
            while pre:
                temp1 = part1.next
                temp2 = pre.next
                part1.next = pre
                pre.next = temp1
                part1 = temp1
                pre = temp2
            