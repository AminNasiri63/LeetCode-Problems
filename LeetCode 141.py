# 141. Linked List Cycle


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




# two pointer method
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sp = fp = head

        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next

            if sp == fp:
                return True

        return False




# set method
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        while head:
            if head in seen:
                return True

            seen.add(head)
            head = head.next

        return False



