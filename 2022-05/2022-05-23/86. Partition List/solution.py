from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        right_head = right = ListNode()
        left_head = left = ListNode(next=head)

        while left.next:
            if left.next.val < x:
                left = left.next
            else:
                right.next = left.next
                right = right.next

                left.next = left.next.next

        left.next = right_head.next
        right.next = None

        return left_head.next
