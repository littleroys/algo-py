from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin = []
        while head:
            bin.append(head.val)
            head = head.next
        sum = 0
        for idx, r in enumerate(bin):
            print(idx, r)
            sum += r * 2 ** (len(bin) - idx - 1)
        return sum


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(0)
    l.next.next = ListNode(1)

    s = Solution()
    print(s.getDecimalValue(l))
