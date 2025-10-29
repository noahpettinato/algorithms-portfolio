# -----------------------------------------------------------------------------
# Homework 4 – PowerSet
# Course: CS 325 – Analysis of Algorithms
# Author: Noah Pettinato
#
# Description:
#   Generates all possible subsets (the power set) of a given input set
#   using a backtracking (recursive) approach.
#
# Key Ideas:
#   • The power set of a set with n elements has 2^n subsets.
#   • The algorithm explores each element's inclusion/exclusion recursively.
#   • Each recursive call builds partial subsets and backtracks to explore
#     alternative combinations.
#   • Time complexity: O(2^n)
# -----------------------------------------------------------------------------

def powerset(inputSet):
    """
    Generate all subsets (the power set) of a given input set.

    Parameters
    ----------
    inputSet : list
        List of elements to generate subsets from.

    Returns
    -------
    list[list]
        A list of all possible subsets of the input set.
    """
    result = []  # Stores all generated subsets

    def backtrack(start, current_subset):
        """
        Recursively builds subsets by exploring each element choice.

        Parameters
        ----------
        start : int
            Current index in the inputSet to consider.
        current_subset : list
            The current subset being constructed.
        """
        # Append a copy of the current subset to the results list
        result.append(current_subset[:])

        # Explore further elements to add to the subset
        for i in range(start, len(inputSet)):
            current_subset.append(inputSet[i])   # Choose element inputSet[i]
            backtrack(i + 1, current_subset)     # Recurse with next index
            current_subset.pop()                 # Backtrack (undo the choice)

    # Start building subsets from the first element
    backtrack(0, [])

    return result
