func rob(nums []int) int {
	n := len(nums)

	if n == 0 {
		return 0
	} else if n == 1 {
		return nums[0]
	} else if n == 2 {
		return max(nums[0], nums[1])
	}

	case1 := robFunc(nums[1:])
	case2 := robFunc(nums[:n-1])

	return max(case1, case2)
}

func robFunc(nums []int) int {
	n := len(nums)
	dp := make([]int, n)
	dp[0], dp[1] = nums[0], max(nums[0], nums[1])

	for i := 2; i < n; i++ {
		dp[i] = max(dp[i-2]+nums[i], dp[i-1])
	}

	return dp[n-1]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}