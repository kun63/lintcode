"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        curr = head
        new_head = None
        while curr:
            
            temp = RandomListNode(curr.label)
            if new_head == None:
                new_head = temp
            if pre:
                pre.next = temp
            pre = temp
            curr.random = (curr.random, temp)
            # change = curr
            curr = curr.next
            # change.next = temp
        curr = head
        curr_new = new_head
        while curr:
            if not curr.random[0]:
                curr_new.random = curr.random[0].random[1]
            curr = curr.next
            curr_new = curr_new.next
        return new_head