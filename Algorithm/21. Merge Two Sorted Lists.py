# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        current_node = start = ListNode() 
        # current_node and start share the same memory address

        while list1 and list2: # neither is None
            if list1.val < list2.val:
                current_node.next = list1 
                # this doesn't change the memory address of current_node
                list1 = list1.next # this will change the memory address
                current_node = current_node.next
            else:
                current_node.next = list2
                list2 = list2.next
                current_node = current_node.next
        
        # now at lease one of list1 and list2 is None
        if list1: # if list1 is not None, list2 is None
            current_node.next = list1
        if list2: # if list2 is not None, list1 is None
            current_node.next = list2
        
        return start.next


'''
Note:
Why is "start" updated when we seem to have done nothing to it?

Here are some examples:
b = 1
print("b id:", id(b))
a = b
print("a id:", id(a))
print("b id:", id(b))
b += 1
print("b id:", id(b))
print(a,b)
>>> b id: 140720860191488
>>> a id: 140720860191488
>>> b id: 140720860191488
>>> b id: 140720860191520
>>> 1 2

listb = [1]
print("listb id:", id(listb))
lista = listb
print("lista id:", id(lista))
print("listb id:", id(listb))
listb.append(2)
print("listb id:", id(listb))
print(lista,listb)
>>> listb id: 1941922543936
>>> lista id: 1941922543936
>>> listb id: 1941922543936
>>> listb id: 1941922543936
>>> [1, 2] [1, 2]

listb = [1]
print("listb id:", id(listb))
lista = listb
print("lista id:", id(lista))
print("listb id:", id(listb))
listb = [1,2]
print("listb id:", id(listb))
print(lista,listb)
>>> listb id: 1771958925504
>>> lista id: 1771958925504
>>> listb id: 1771958925504
>>> listb id: 1771957660608
>>> [1] [1, 2]

As we can see from the example, id() prints out the memory address of a variable.
Methods like append() to a list does not change the memory address.
Therefore, if two lists share the same address, their value change at the same time.
While giving the variable a new value will change the address too,
therefore has no effect on other variables who used to share the address.
'''
