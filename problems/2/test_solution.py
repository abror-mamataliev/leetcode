from solution import Solution


def test():
    solution = Solution()
    inputs = [
        [[2,4,3], [5,6,4]],
        [[0], [0]],
        [[9,9,9,9,9,9,9], [9,9,9,9]]
    ]
    targets = [
        [7,0,8],
        [0],
        [8,9,9,9,0,0,0,1]
    ]
    i = 1
    for input, target in zip(inputs, targets):
        assert solution.solve(*input) == target, f"Test {i} failed"
        i += 1
