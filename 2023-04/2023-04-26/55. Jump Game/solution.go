func canJump(nums []int) bool {
    n := len(nums)

    last := n - 1
    for i := n - 2; i >= 0; i-- {
        if nums[i] + i >= last {
            last = i
        }
    }

    return last == 0
}