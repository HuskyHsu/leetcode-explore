from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def _reverse(self, head: ListNode) -> ListNode:
        curr = head

        while curr.next:
            temp = curr.next
            curr.next = curr.next.next
            temp.next = head
            head = temp

        return head

    def _find_mid(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head is None or head.next is None:
            return

        slow = self._find_mid(head)

        l1 = head
        l2 = slow.next
        slow.next = None

        l2 = self._reverse(l2)

        while l1 and l2:
            temp = l2.next
            l2.next = l1.next
            l1.next = l2
            l1 = l1.next.next
            l2 = temp
