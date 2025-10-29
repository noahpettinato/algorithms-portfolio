# -----------------------------------------------------------------------------
# Homework 4 – MaxSet
# Course: CS 325 – Analysis of Algorithms
# Author: Noah Pettinato
#
# Description:
#   Finds the maximum-sum subset of a list of integers such that
#   no two chosen elements are adjacent in the original list.
#
#   This is a variation of the "Maximum Weighted Independent Set"
#   problem for a path graph, commonly solved with Dynamic Programming.
#
# Key Ideas:
#   • Use DP to store the best achievable sum up to each index.
#   • Transition: dp[i] = max(dp[i−1], dp[i−2] + nums[i−1])
#   • Reconstruct the optimal subset by tracing back through dp[].
#   • Time complexity: O(n)
#   • Space complexity: O(n)
# -----------------------------------------------------------------------------

def max_independent_set(nums):
    """
    Compute the maximum-sum subset of non-adjacent elements.

    Parameters
    ----------
    nums : list[int]
        Input list of integers.

    Returns
    -------
    list[int]
        Subset of nums representing the maximum independent set.
    """
    if not nums:
        return []  # Empty input case

    n = len(nums)

    # Initialize DP array: dp[i] = max sum using first i elements
    dp = [0] * (n + 1)
    dp[1] = max(0, nums[0])

    # Fill DP table
    for i in range(2, n + 1):
        # Option 1: exclude current element → dp[i−1]
        # Option 2: include current element → dp[i−2] + nums[i−1]
        dp[i] = max(dp[i - 1], dp[i - 2] + max(nums[i - 1], 0))

    # Reconstruct the chosen subset by tracing backward
    subsequence = []
    i = n
    while i > 0:
        if dp[i] == dp[i - 1]:
            i -= 1
        else:
            subsequence.append(nums[i - 1])
            i -= 2  # Skip adjacent element

    # Edge case: if all negatives and 0 present, return [0]
    if not subsequence and 0 in nums:
        return [0]

    # Reverse since reconstruction goes backward
    return subsequence[::-1]
