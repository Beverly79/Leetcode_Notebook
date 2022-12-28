# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # two pointers, fast to find x first
        # slow stays at the begining
        # then slow goes to the first larger than or equal to x
        # from x, if fast sees a node smaller than x, put it in front of slow
        # ends when fast goes to the end

        if head == None or head.next == None:
            return head


        fix = move = dummy = ListNode(-200,head)
        # fix is to find where to insert the small nodes
        while fix.next:
            if fix.next.val >= x: # fix is the node before the first big node
                break
            fix = fix.next
            move = move.next # at this point, move is the same as fix
        
        # we start from the move to make sure every small node after fix is inserted before fix
        while move.next:
            if move.next.val < x: # the node after move should be inserted
                fix.next = ListNode(val=move.next.val,next=fix.next)
                fix = fix.next # preserve the original relative order so go to next
                move.next = move.next.next # move.next deleted
            else:
                move = move.next # no need to do anything just go on
        return dummy.next
        # why not return head?
        # at the beginning 
        # head shared the same memory address with fix.next and move.next
        # but changing fixed.next or move.next will change the address
        # therefore it does nothing to head.
        # however, dummy and fix and move have the same address
        # changing fixed.next and move.next doesn't change address
        # therefore changes dummy at the same time

