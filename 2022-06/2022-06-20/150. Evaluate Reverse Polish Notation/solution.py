from typing import List


class Solution:
    def calc(self, operand, n1: int, n2: int) -> int:
        if operand == "+":
            return n1 + n2

        if operand == "-":
            return n1 + -n2

        if operand == "*":
            return n1 * n2

        if operand == "/":
            return int(n1 / n2)

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for token in tokens:
            if token in "+-*/":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(self.calc(token, n1, n2))
                continue

            stack.append(int(token))

        return stack[0]
