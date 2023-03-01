/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func reverseList(head *ListNode) *ListNode {
    if head == nil {
        return head
    }

    cur := head
    for cur.Next != nil {
        temp := cur.Next
        cur.Next = cur.Next.Next
        temp.Next = head
        head = temp
    }

    return head
}