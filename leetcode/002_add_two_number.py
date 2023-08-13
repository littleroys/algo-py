# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = cur = ListNode()
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            cur.next = ListNode(val=(val1 + val2 + carry) % 10)
            carry = (val1 + val2 + carry) // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next
        if carry != 0:
            cur.next = ListNode(1)
        return dummy.next


class Solution1:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = cur = ListNode()
        carry = 0
        while l1 or l2:
            cur.next = l1 if l1 else l2
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            print("val1 =>", val1, "val2=>", val2)
            cur.next.val = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next
        if carry != 0:
            cur.next = ListNode(1)

        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(3)

    l2 = ListNode(9)
    l2.next = ListNode(8)
    l2.next.next = ListNode(4)

    s = Solution1()
    result = s.addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next
