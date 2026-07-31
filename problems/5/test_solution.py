from solution import Solution


def test():
    solution = Solution()
    inputs = [
        ("babad",),
        ("cbbd",)
    ]
    targets = [
        "bab",
        "bb"
    ]
    i = 1
    for input, target in zip(inputs, targets):
        assert solution.solve(*input) == target, f"Test {i} failed"
        i += 1
