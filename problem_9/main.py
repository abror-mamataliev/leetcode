from importlib import import_module


log = import_module("utils", "..").log


@log
def isPalindrome(x: int) -> bool:
    """
    Given an integer, write a function to determine if it is a palindrome.
    
    Example:
    Input: 121
    Output: true
    
    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    
    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    
    :param x: int - the integer to check if it is a palindrome
    :return: bool - True if the integer is a palindrome, False otherwise
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """


def run():
    isPalindrome(x=121)
    isPalindrome(x=-121)
    isPalindrome(x=10)
