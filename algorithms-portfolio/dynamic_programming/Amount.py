def amount(A, S):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return

        for i in range(start, len(A)):
            # Avoid duplicate combinations by skipping the same amount value
            if i > start and A[i] == A[i - 1]:
                continue
            # Explore further combinations
            backtrack(i + 1, target - A[i], path + [A[i]])

    result = []
    A.sort()  # Sorting to handle duplicates
    backtrack(0, S, [])
    return result