from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        while head:
            if head.val != val:
                cur.next = head
                cur = cur.next
            head = head.next
        cur.next = None
        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1) 
    l1.next = ListNode(2) 
    l1.next.next = ListNode(6) 
    l1.next.next.next = ListNode(6) 
    l1.next.next.next.next = ListNode(6) 

    s = Solution()
    result = s.removeElements(l1, 6)
    while result:
        print(result.val)
        result = result.next 
