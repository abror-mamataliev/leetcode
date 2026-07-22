from solution import Solution


def test():
    solution = Solution()
    inputs = [
        [[2, 7, 11, 15], 9],
        [[3, 2, 4], 6],
        [[3, 3], 6]
    ]
    targets = [
        [0, 1],
        [1, 2],
        [0, 1]
    ]
    i = 1
    for input, target in zip(inputs, targets):
        assert solution.solve(*input) == target, f"Test {i} failed"
        i += 1
