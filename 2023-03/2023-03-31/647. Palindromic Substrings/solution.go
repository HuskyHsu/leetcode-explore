func countSubstrings(s string) int {
	n := len(s)
	if n == 1 {
		return n
	}

	dp := make([][]bool, n)
	for i, _ := range dp {
		dp[i] = make([]bool, n)
		dp[i][i] = true
	}

	count := n
	for l := 2; l <= n; l++ {
		for i := 0; i <= n-l; i++ {
			j := i + l - 1
			if s[i] == s[j] && (l == 2 || dp[i+1][j-1]) {
				count += 1
				dp[i][j] = true
			}
		}
	}

	return count
}