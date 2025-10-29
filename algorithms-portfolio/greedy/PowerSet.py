def powerset(inputSet):
    result = []  # Initialize an empty list to store the subsets
    def backtrack(start, current_subset):
        result.append(current_subset[:])  # Append a copy of the current subset to the 'result' list
        for i in range(start, len(inputSet)):
            current_subset.append(inputSet[i])  # Include the current element in the subset
            backtrack(i + 1, current_subset)    # Recur with the next index
            current_subset.pop()                # Backtrack by removing the current element
    backtrack(0, [])  # Start the backtracking process from the beginning
    return result