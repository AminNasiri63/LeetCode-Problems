# 206. Reverse Linked List


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        tail = None

        while cur:
            temp = cur.next
            cur.next = tail
            tail = cur
            cur = temp

        return tail



