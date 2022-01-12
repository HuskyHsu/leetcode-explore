class Solution:
    def __init__(self):
        self.cache = {
            0: 0,
            1: 1
        }

    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]

        result = self.fib(n - 1) + self.fib(n - 2)
        self.cache[n] = result
        return result
