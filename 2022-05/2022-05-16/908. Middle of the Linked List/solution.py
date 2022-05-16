from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        total = 0
        current = head

        while current.next is not None:
            total += 1
            current = current.next

        for _ in range(total // 2 + 1 if total % 2 == 1 else total // 2):
            head = head.next

        return head
