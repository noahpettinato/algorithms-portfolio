# -----------------------------------------------------------------------------
# Homework 3 – DNAMatch
# Course: CS 325 – Analysis of Algorithms
# Author: Noah Pettinato
#
# Description:
#   Implements two versions (Top-Down and Bottom-Up) of the Dynamic
#   Programming algorithm for finding the Longest Common Subsequence (LCS)
#   between two DNA strings. The LCS represents the longest sequence of
#   nucleotides appearing in both DNA sequences in the same order (not
#   necessarily contiguous).
#
# Key Ideas:
#   • Uses a 2D DP table (m+1 x n+1) where dp[i][j] stores the length
#     of the LCS between DNA1[:i] and DNA2[:j].
#   • Recurrence relation:
#       if DNA1[i-1] == DNA2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
#       else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#   • Time complexity: O(m * n)
#   • Space complexity: O(m * n)
# -----------------------------------------------------------------------------

def dna_match_topdown(DNA1, DNA2):
    """
    Computes the LCS length between two DNA sequences using a
    top-down dynamic programming approach.

    Parameters
    ----------
    DNA1 : str
        First DNA sequence.
    DNA2 : str
        Second DNA sequence.

    Returns
    -------
    int
        Length of the longest common subsequence.
    """
    m, n = len(DNA1), len(DNA2)

    # Initialize 2D DP table with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table row by row
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match, add 1 to the diagonal value
            if DNA1[i - 1] == DNA2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # Otherwise, take the max of left and top values
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def dna_match_bottomup(DNA1, DNA2):
    """
    Computes the LCS length between two DNA sequences using a
    bottom-up dynamic programming approach.

    (In this implementation, the logic is equivalent to the top-down
    version since both iteratively fill a DP table.)

    Parameters
    ----------
    DNA1 : str
        First DNA sequence.
    DNA2 : str
        Second DNA sequence.

    Returns
    -------
    int
        Length of the longest common subsequence.
    """
    m, n = len(DNA1), len(DNA2)

    # Initialize DP table with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the table iteratively
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if DNA1[i - 1] == DNA2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]
