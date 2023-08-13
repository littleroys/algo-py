from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n == 1:
            return None
        cur = end = head
        length = 1
        while end.next:
            end = end.next
            length += 1

        length = length - n - 1
        # handle this case: [1]->[2], n=2
        if length == -1:
            head = cur.next
            return head
        while length > 0:
            cur = cur.next
            length -= 1
        cur.next = cur.next.next

        return head


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    # l.next.next = ListNode(3)
    # l.next.next.next = ListNode(4)
    # l.next.next.next.next = ListNode(5)
    # l.next.next.next.next.next = ListNode(6)

    s = Solution()
    result = s.removeNthFromEnd(l, 2)
    while result:
        print(result.val)
        result = result.next
