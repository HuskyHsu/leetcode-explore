import "fmt"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}

	var output [][]int
	var stack = make([]*TreeNode, 0)

	stack = append(stack, root)
	fmt.Println(stack)

	for len(stack) > 0 {
		var sub_result []int
		stack_len := len(stack)
		for i := 0; i < stack_len; i++ {
			item := stack[i]
			sub_result = append(sub_result, item.Val)

			if item.Left != nil {
				stack = append(stack, item.Left)
			}
			if item.Right != nil {
				stack = append(stack, item.Right)
			}
		}

		stack = stack[stack_len:]
		output = append(output, sub_result)
	}

	return output
}