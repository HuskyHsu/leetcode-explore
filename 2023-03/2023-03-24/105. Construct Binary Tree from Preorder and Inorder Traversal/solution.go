// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func index(arr []int, target int) int {
	for i, v := range arr {
		if v == target {
			return i
		}
	}
	return -1
}

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder)+len(inorder) == 0 {
		return nil
	}

	root := &TreeNode{Val: preorder[0]}

	mid_index := index(inorder, preorder[0])
	root.Left = buildTree(preorder[1:mid_index+1], inorder[:mid_index])
	root.Right = buildTree(preorder[mid_index+1:], inorder[mid_index+1:])

	return root
}

