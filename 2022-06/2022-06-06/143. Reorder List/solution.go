/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func reorderList(head *ListNode)  {
	 slow := head
	 fast := head.Next

	 for fast != nil && fast.Next != nil {
		 fast = fast.Next.Next
		 slow = slow.Next
	 }

	 secondHalf := reverse(slow)
	 slow.Next = nil

	 fmt.Println(secondHalf)

	 cur := head
	 for cur != nil && secondHalf != nil {
		 next := cur.Next
		 secondHalfNext := secondHalf.Next

		 cur.Next = secondHalf
		 secondHalf.Next = next

		 cur = next
		 secondHalf = secondHalfNext
	 }

 }

 func reverse(head *ListNode) *ListNode {
	 cur := head
	 for cur.Next != nil {
		 temp := cur.Next
		 cur.Next = temp.Next
		 temp.Next = head
		 head = temp
	 }

	 return head
 }