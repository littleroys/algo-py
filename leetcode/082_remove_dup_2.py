from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(ptr):
            counter = 0
            while ptr.next and (ptr.val == ptr.next.val):
                ptr = ptr.next
                counter += 1
            return ptr, counter

        dummy = cur = ListNode(None)
        while cur and head:
            head, counter = helper(head)
            if counter == 0:
                cur.next,cur = head, head
            head = head.next
        cur.next = head
        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(1)
    l1.next.next.next = ListNode(1)
    l1.next.next.next.next = ListNode(3)
    l1.next.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next.next.next = ListNode(5)

    s = Solution()
    res = s.deleteDuplicates(l1)
    while res:
        print(res.val)
        res = res.next
