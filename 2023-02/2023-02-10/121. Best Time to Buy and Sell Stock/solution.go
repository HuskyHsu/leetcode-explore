func maxProfit(prices []int) int {
    maxDiff := 0
    lowest := prices[0]

    for _, price := range prices {
        if price > lowest {
            localDiff := price - lowest
            if (localDiff > maxDiff) {
                maxDiff = localDiff
            }
        } else if price < lowest {
            lowest = price
        }
    }
    return maxDiff
}