from solution import Solution


def test():
    solution = Solution()
    inputs = [
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
        ("A", 1),
        ("AB", 1),
        ("ABC", 1)
    ]
    targets = [
        "PAHNAPLSIIGYIR",
        "PINALSIGYAHRPI",
        "A",
        "AB",
        "ABC"
    ]
    i = 1
    for input, target in zip(inputs, targets):
        assert solution.solve(*input) == target, f"Test {i} failed"
        i += 1
