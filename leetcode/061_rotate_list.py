from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        To be a circle, and refresh new head by moving (length - k%length)
        """
        if head is None:
            return head

        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head

        k = length - (k % length)
        while k > 0:
            cur = cur.next
            k -= 1
        head = cur.next
        cur.next = None
        return head


if __name__ == "__main__":
    l1 = None
    s = Solution()
    result = s.rotateRight(l1, 1)
