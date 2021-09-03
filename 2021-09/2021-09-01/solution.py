class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_depth = 0
        flags = [False]*len(nums)
        for n in nums:
            steps = 0
            while flags[n] == False:
                flags[n] = True
                steps += 1
                n = nums[n]
            max_depth = max(steps, max_depth)

        return max_depth
