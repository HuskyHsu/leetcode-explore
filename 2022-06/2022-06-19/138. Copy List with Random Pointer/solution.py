from typing import Optional, Self


class Node:
    def __init__(self, x: int, next: Self = None, random: Self = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None

        curr = head
        output = Node(0)
        output_h = output

        random_map = {}

        while curr:
            output.next = Node(curr.val)

            if curr.random:
                if curr.random not in random_map:
                    random_map[curr.random] = []
                random_map[curr.random].append(output.next)

            curr = curr.next
            output = output.next

        temp_o = output_h.next
        temp_h = head
        while temp_h:
            if temp_h in random_map:
                for node in random_map[temp_h]:
                    node.random = temp_o

            temp_o = temp_o.next
            temp_h = temp_h.next

        return output_h.next
