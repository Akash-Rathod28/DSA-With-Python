class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head 
        fast = head
        hasCycle = False

        # Step 1: Detect cycle
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCycle = True
                break

        # Step 2: If no cycle
        if not hasCycle:
            return None

        # Step 3: Find cycle length
        l = 0
        while slow.next != fast:
            slow = slow.next
            l += 1
        l += 1
        slow = slow.next

        # Step 4: Find start of cycle
        slow = head
        fast = head
        for i in range(l):
            fast = fast.next

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
