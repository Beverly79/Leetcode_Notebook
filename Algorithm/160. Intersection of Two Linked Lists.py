# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


########### Time O(n+m)  Space O(n) ###########
class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set() # Why will it exceed time limit if we use list to store the node?
        # set is way gaster than list, but it takes up more storage room as well.
        curr = headA
        while curr: # stops when headA goes to the end
            s.add(curr) # add everything in list A into the set
            curr = curr.next
        curr = headB
        while curr:
            if curr in s: # check if the node in list B is in the set
                return curr 
            curr = curr.next
        return None


########### Time O(n+m)  Space O(n) ###########
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        '''
        two pointer to save more space
        we assume one is listA + listB, two is listB + listA
        one goes through listA and goes to listB
        in such case, if listA and listB intersect
        and the length of one and two will go through is the same,
        one and two will meet in the end.
        if no intersection,
        one and two will go to the end and become None.
        '''

        one = headA
        two = headB
        while one != two: # stops when they are the same
            if one == None: # one goes to the end of listA
                one = headB # start from B
            else:
                one = one.next
            if two == None:
                two = headA
            else:
                two = two.next
        # one and two must be the same in the end
        # case 1: they intersect, one and two are both the intersection node
        # case 2: no intersect, one and two are both None
        return one # or return two