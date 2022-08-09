from importlib import import_module


log = import_module("utils", "..").log


@log
def romanToInt(s: str) -> int:
    """
    Given a roman numeral, convert it to an integer.

    Example:
    Input: "III"
    Output: 3
    
    Input: "LVIII"
    Output: 58

    Input: "MCMXCIV"
    Output: 1994
    
    :param s: str - the roman numeral to convert to an integer
    :return: int - the integer representation of the roman numeral

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    pass


def run():
    romanToInt(s="III")
    romanToInt(s="LVIII")
    romanToInt(s="MCMXCIV")
