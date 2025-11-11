class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: #type: ignore
        while(head is not None):
            if head.val is None:
                return True
            head.val = None
            head = head.next
        else:
            return False