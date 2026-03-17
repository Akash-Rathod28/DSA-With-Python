class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        
        while curr:
            length += 1
            curr = curr.next
        
        r = length - n
        
        
        if r == 0:
            return head.next
        
        curr = head
        
        for i in range(r - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        
        return head
