from solution import Solution


def test():
    solution = Solution()
    inputs = [
        ("()",),
        ("()[]{}",),
        ("(]",),
        ("([])",),
        ("([)]",)
    ]
    targets = [
        True,
        True,
        False,
        True,
        False
    ]
    i = 1
    for input, target in zip(inputs, targets):
        assert solution.solve(*input) == target, f"Test {i} failed"
        i += 1
