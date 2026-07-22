"""
Approach:
    (write your approach here)

Time complexity:  O(?)
Space complexity: O(?)
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        overflow = 0
        result = ListNode()
        voyager = ListNode(0, result)
        while l1 is not None or l2 is not None:
            voyager = voyager.next
            sum = (
                (l1.val if l1 is not None else 0)
                + (l2.val if l2 is not None else 0)
                + overflow
            )
            overflow = sum // 10
            voyager.val = sum % 10
            voyager.next = ListNode()
            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        voyager.next = ListNode(overflow) if overflow > 0 else None
        return result
