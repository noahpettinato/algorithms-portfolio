# -----------------------------------------------------------------------------
# Homework 2 – KthElement
# Course: CS 325 – Analysis of Algorithms
# Author: Noah Pettinato
#
# Description:
#   Finds the k-th smallest element in the union of two sorted arrays.
#   This is a classic divide-and-conquer algorithm similar to the
#   "median of two sorted arrays" problem. It recursively discards
#   portions of the arrays that cannot contain the desired element.
#
# Key Ideas:
#   • Both arrays are assumed to be sorted in ascending order.
#   • At each step, the algorithm compares elements near the k/2 mark
#     and discards the smaller portion that cannot contain the k-th element.
#   • Runs in O(log k) time complexity on average.
# -----------------------------------------------------------------------------

def kthElement(Arr1, Arr2, k):
    """
    Recursively find the k-th smallest element in two sorted arrays.

    Parameters
    ----------
    Arr1 : list
        First sorted array.
    Arr2 : list
        Second sorted array.
    k : int
        1-based index of the desired element in the combined sorted order.

    Returns
    -------
    int or float
        The k-th smallest element in the combined arrays.
    """

    m = len(Arr1)
    n = len(Arr2)

    # Ensure Arr1 is the shorter array to simplify logic
    if m > n:
        return kthElement(Arr2, Arr1, k)

    # Base cases
    if m == 0:
        # If Arr1 is empty, the k-th element is in Arr2
        return Arr2[k - 1]

    if k == 1:
        # If k == 1, return the smallest of the two first elements
        return min(Arr1[0], Arr2[0])

    # Split k between the two arrays
    i = min(m, k // 2)
    j = k - i

    # Compare the elements just before the split positions
    if Arr1[i - 1] < Arr2[j - 1]:
        # Discard first i elements of Arr1 and adjust k
        return kthElement(Arr1[i:], Arr2, k - i)
    else:
        # Discard first j elements of Arr2 and adjust k
        return kthElement(Arr1, Arr2[j:], k - j)
