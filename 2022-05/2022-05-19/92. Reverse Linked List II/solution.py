from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if head is None:
            return head

        dummy = ListNode(next=head)
        curr = dummy

        for _ in range(left - 1):
            curr = curr.next

        start = curr.next
        for _ in range(right - left):
            tmp = start.next
            start.next = tmp.next
            tmp.next = curr.next
            curr.next = tmp

        return dummy.next
