from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        curr = head
        while curr.next:
            temp = curr.next
            curr.next = curr.next.next
            temp.next = head
            head = temp

        return head
