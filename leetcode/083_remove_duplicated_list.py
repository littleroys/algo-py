from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(None)
        while head:
            if cur.val != head.val:
                cur.next = head
                cur = cur.next
            head = head.next
        cur.next = None
        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(2)
    l1.next.next.next.next = ListNode(3)
    l1.next.next.next.next.next = ListNode(3)
    l1.next.next.next.next.next.next = ListNode(3)

    s = Solution()
    s.deleteDuplicates(l1)

    while l1:
        print(l1.val)
        l1 = l1.next
