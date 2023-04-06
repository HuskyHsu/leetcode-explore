func insert(intervals [][]int, newInterval []int) [][]int {
	result := [][]int{}

	newStart, newEnd := newInterval[0], newInterval[1]
	hasInsert := false

	for _, item := range intervals {
		curStart, curEnd := item[0], item[1]

		if curEnd < newStart {
			result = append(result, item)
		} else if curStart > newEnd {
			if !hasInsert {
				result = append(result, []int{newStart, newEnd})
				hasInsert = true
			}
			result = append(result, item)
		} else {
			if curStart <= newStart && newStart <= curEnd {
				newStart = curStart
			}

			if curStart <= newEnd && newEnd <= curEnd {
				newEnd = curEnd
			}
		}
	}

	if !hasInsert {
		result = append(result, []int{newStart, newEnd})
	}

	return result
}