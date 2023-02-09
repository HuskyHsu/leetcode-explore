func maxArea(height []int) int {
    l := 0
    r := len(height) - 1
    maxArea := 0

    for l < r {
        area := r-l
        if height[r] < height[l] {
            area *= height[r]
            r--
        } else {
            area *= height[l]
            l++
        }
        if area > maxArea {
            maxArea = area
        }
    }
    return maxArea
}