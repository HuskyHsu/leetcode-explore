from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        N = len(nums)

        results = []
        for i in range(N - 2):
            point_l = i + 1
            point_r = N - 1

            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while point_l < point_r:
                sum_num = nums[i] + nums[point_l] + nums[point_r]
                if sum_num == 0:
                    results.append([nums[i], nums[point_l], nums[point_r]])
                    point_l += 1
                    point_r -= 1
                    while point_l < point_r and nums[point_l] == nums[point_l - 1]:
                        point_l += 1

                    while point_l < point_r and nums[point_r] == nums[point_r + 1]:
                        point_r -= 1

                elif sum_num > 0:
                    point_r -= 1

                elif sum_num < 0:
                    point_l += 1

        return results
