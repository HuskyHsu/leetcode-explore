func climbStairs(n int) int {
	one, two := 1, 2

	for i := 0; i < n-1; i++ {
		sum := one + two
		one, two = two, sum
	}

	return one
}