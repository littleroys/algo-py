from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        start = dummy = ListNode(0)
        dummy.next = head
        step = right - left
        while left > 1:
            start = start.next
            left -= 1
        cur = prev = start
        cur = cur.next
        while step >= 0:
            # reverse nodes
            cur, tmp = cur.next, cur
            prev, tmp.next = tmp, prev
            step -= 1
        start.next.next = cur
        start.next = prev

        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    # l1.next.next = ListNode(3)
    # l1.next.next.next = ListNode(4)
    # l1.next.next.next.next = ListNode(5)
    # l1.next.next.next.next.next = ListNode(6)

    s = Solution()
    res = s.reverseBetween(l1, 1, 2)

    while res:
        print(res.val)
        res = res.next
