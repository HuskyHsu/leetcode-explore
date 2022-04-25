from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for n in nums:
            output += [item + [n] for item in output]

        return output