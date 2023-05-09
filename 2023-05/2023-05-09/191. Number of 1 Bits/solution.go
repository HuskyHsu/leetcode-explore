// You can edit this code!
// Click here and start typing.
package main

import "fmt"

func hammingWeight(num uint32) int {
    result := 0
    for num > 0 {
        num &= num - 1
        result += 1
    }

    return result
}