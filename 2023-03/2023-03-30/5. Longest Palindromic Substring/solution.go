func longestPalindrome(s string) string {
	n := len(s)
	if n < 2 {
		return s
	}

	dp := make([][]bool, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]bool, n)
		dp[i][i] = true
	}

	left, right := 0, 0
	for l := 2; l <= n; l++ {
		for i := 0; i < n-l+1; i++ {
			j := i + l - 1
			if s[i] == s[j] && (l == 2 || dp[i+1][j-1]) {
				dp[i][j] = true
				if l > right-left+1 {
					left, right = i, j
				}
			}
		}
	}

	return s[left : right+1]
}