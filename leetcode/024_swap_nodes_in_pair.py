from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = dummy = ListNode(0)
        while head and head.next:
            p.next = head.next
            p = head
            head = head.next.next
            p.next.next = p
        p.next = head
        return dummy.next


if __name__ == "__main__":
    l = ListNode(1)
    # l.next = ListNode(2)
    # l.next.next = ListNode(3)
    # l.next.next.next = ListNode(4)

    s = Solution()
    res = s.swapPairs(l)
    while res:
        print(res.val)
        res = res.next
