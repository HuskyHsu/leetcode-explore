func lengthOfLongestSubstring(s string) int {
    lastSeen := make(map[rune]int)
    start := 0
    longest := 0

    for i, c := range s {
        if lastIndex, ok := lastSeen[c]; ok && lastIndex >= start {
            start = lastIndex + 1
        }
        lastSeen[c] = i
        if i - start + 1 > longest {
            longest = i - start + 1
        }
    }

    return longest
}