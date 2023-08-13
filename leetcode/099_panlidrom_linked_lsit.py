from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Stack Solution
class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next
        return True


class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr

        while prev:
            if head.val != prev.val:
                return False
            prev = prev.next
            head = head.next
        return True


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)
    list1.next.next.next = ListNode(3)
    list1.next.next.next.next = ListNode(1)

    s1 = Solution1()
    print(s1.isPalindrome(list1))

    s2 = Solution2()
    print(s2.isPalindrome(list1))