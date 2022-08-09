from importlib import import_module
from typing import Optional


log = import_module("utils", "..").log


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        if self.next is not None:
            return f"{self.val} -> {self.next}"
        else:
            return f"{self.val}"


@log()
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

    :param l1: ListNode - the first linked list
    :param l2: ListNode - the second linked list
    :return: ListNode - the sum of the two linked lists

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    pass


def run():
    addTwoNumbers(l1=ListNode(2, ListNode(4, ListNode(3))), l2=ListNode(5, ListNode(6, ListNode(4))))
    addTwoNumbers(l1=ListNode(), l2=ListNode())
    addTwoNumbers(l1=ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), l2=ListNode(9, ListNode(9, ListNode(9))))
