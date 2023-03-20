type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func validBST(root, min, max *TreeNode) bool {
	if root == nil {
		return true
	}

	if min != nil && min.Val >= root.Val {
		return false
	}

	if max != nil && max.Val <= root.Val {
		return false
	}

	return validBST(root.Left, min, root) && validBST(root.Right, root, max)
}

func isValidBST(root *TreeNode) bool {
	return validBST(root, nil, nil)
}