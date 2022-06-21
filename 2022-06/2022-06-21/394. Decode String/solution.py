class Solution:
    def decodeString(self, s: str) -> str:
        stack_c = [""]
        stack_n = []
        num_s = ""

        for c in s:
            if c in "0123456789":
                num_s += c

            elif c == "[":
                stack_n.append(int(num_s))
                stack_c.append("")
                num_s = ""

            elif c == "]":
                c_s = stack_c.pop()
                stack_c[-1] += c_s * stack_n.pop()

            else:
                stack_c[-1] += c

        return stack_c[0]
