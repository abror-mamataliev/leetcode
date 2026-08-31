from solution import Solution


def test():
    solution = Solution()
    inputs = [
        (123,),
        (-123,),
        (120,),
    ]
    targets = [
        321,
        -321,
        21,
    ]
    i = 1
    for input, target in zip(inputs, targets):
        assert solution.solve(*input) == target, f"Test {i} failed"
        i += 1
