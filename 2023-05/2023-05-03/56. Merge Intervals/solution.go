import (
    "fmt"
    "sort"
)

func merge(intervals [][]int) [][]int {
    var result [][]int

    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })

    currEnd := -1

    for _, interval := range intervals {
        start, end := interval[0], interval[1]

        if start <= currEnd {
            if end > currEnd {
                result[len(result) - 1][1] = end
                currEnd = end
            }
        } else {
            result = append(result, interval)
            currEnd = end
        }
    }

    return result
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}