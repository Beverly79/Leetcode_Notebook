"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        newhead = Node(x=head.val, next=Node(x=0), random=Node(x=0))
        new = newhead
        old = head
        dic = {}
        while old:
            new.val = old.val # copy val
            dic[old] = new # add old node as the key, new node as the value
            new.next = Node(x=0)
            new = new.next # move to next
            old = old.next
            

        # start over, now every node is in the dictionary so we can add random
        new = newhead
        old = head

        while old.next:
            if old.random != None:
                new.random = dic[old.random]
            else:
                new.random = None
            old = old.next
            new = new.next
        
        # the last one in new is Node(0), should delete it
        #new.next = None
        new.next = None
        if old.random != None:
            new.random = dic[old.random]
        else:
            new.random = None

        return newhead