func isValid(s string) bool {
    pares := map[rune]rune{
        ')': '(',
        '}': '{',
        ']': '[',
    }

    stack := make([]rune, 0)

    for _, char := range s {
        _, ok := pares[char]
        if ok {
            if len(stack) > 0 && stack[len(stack) - 1] == pares[char] {
                stack = stack[:len(stack) - 1]
            } else {
                return false
            }
        } else {
            stack = append(stack, char)
        }
    }

    return len(stack) == 0
}