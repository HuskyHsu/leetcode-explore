func characterReplacement(s string, k int) int {
    start := 0

    counter := make([]int, 26)
    maxCount := 0
    maxLen := 0

    for i, _ := range s {
        counter[s[i]-'A'] += 1
        maxCount = max(maxCount, counter[s[i]-'A'])

        if i - start + 1 > k + maxCount {
            counter[s[start]-'A'] -= 1
            start += 1
        }
        maxLen = max(maxLen, i - start + 1)
    }

    return maxLen
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}