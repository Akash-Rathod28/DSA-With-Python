# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        
        # count length
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        # middle index (second middle automatically)
        mid = length // 2
        
        # move to middle
        curr = head
        for i in range(mid):
            curr = curr.next
        
        return curr
