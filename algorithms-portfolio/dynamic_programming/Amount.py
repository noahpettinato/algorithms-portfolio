# -----------------------------------------------------------------------------
# Homework 5 – Amount
# Course: CS 325 – Analysis of Algorithms
# Author: Noah Pettinato
#
# Description:
#   Finds all unique combinations of elements in a list A that sum to a
#   specified target value S. Each element in A may be used at most once.
#
# Key Ideas:
#   • Uses backtracking to explore possible combinations.
#   • Prunes branches when the running total exceeds the target.
#   • Skips duplicate elements (after sorting) to avoid repeated combinations.
#   • Time complexity: O(2^n) in the worst case (subset enumeration).
# -----------------------------------------------------------------------------

def amount(A, S):
    """
    Find all unique subsets of A that sum to a target value S.

    Parameters
    ----------
    A : list[int]
        List of available amounts (can contain duplicates).
    S : int
        Target sum value.

    Returns
    -------
    list[list[int]]
        List of subsets that sum to S.
    """

    def backtrack(start, target, path):
        """
        Recursive helper to explore valid subsets.

        Parameters
        ----------
        start : int
            Index to start exploring from.
        target : int
            Remaining sum to achieve.
        path : list[int]
            Current combination of elements being considered.
        """
        # Base case: exact match found
        if target == 0:
            result.append(path)
            return

        # Prune if the remaining target is negative
        if target < 0:
            return

        # Explore subsequent elements
        for i in range(start, len(A)):
            # Skip duplicates to avoid redundant combinations
            if i > start and A[i] == A[i - 1]:
                continue

            # Choose current element and recurse
            backtrack(i + 1, target - A[i], path + [A[i]])

    # Sort input to handle duplicates efficiently
    result = []
    A.sort()
    backtrack(0, S, [])
    return result
