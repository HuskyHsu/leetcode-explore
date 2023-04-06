func maxSubArray(nums []int) int {
	curSum := 0
	maxSum := nums[0]

	for _, v := range nums {
		curSum += v
		if curSum > maxSum {
			maxSum = curSum
		}

		if curSum < 0 {
			curSum = 0
		}
	}

	return maxSum
}