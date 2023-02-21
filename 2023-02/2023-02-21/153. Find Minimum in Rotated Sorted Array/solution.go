func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}

func searchMin(nums []int) int {
    if len(nums) == 1 {
        return nums[0]
    }
    mid := len(nums) / 2
    return min(searchMin(nums[:mid]), searchMin(nums[mid:]))
}

func findMin(nums []int) int {
    return searchMin(nums)
}