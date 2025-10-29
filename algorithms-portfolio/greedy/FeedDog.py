# -----------------------------------------------------------------------------
# Homework 5 – FeedDog
# Course: CS 325 – Analysis of Algorithms
# Author: Noah Pettinato
#
# Description:
#   Determines the maximum number of dogs that can be satisfied by
#   assigning each dog at most one biscuit. A dog is satisfied if its
#   hunger level is less than or equal to the size of the biscuit it receives.
#
# Key Ideas:
#   • Sort both hunger levels and biscuit sizes in ascending order.
#   • Greedily assign the smallest possible biscuit that satisfies each dog.
#   • If a biscuit is too small, move to the next one.
#   • Time complexity: O(n log n) due to sorting.
# -----------------------------------------------------------------------------

def feedDog(hunger_level, biscuit_size):
    """
    Compute the maximum number of dogs that can be satisfied with given biscuits.

    Parameters
    ----------
    hunger_level : list[int]
        List representing each dog's hunger requirement.
    biscuit_size : list[int]
        List representing the sizes of available biscuits.

    Returns
    -------
    int
        Maximum number of dogs that can be satisfied.
    """

    # Sort hunger levels and biscuit sizes for greedy pairing
    hunger_level.sort()
    biscuit_size.sort()

    satisfied_dogs = 0
    biscuit_index = 0

    # Assign biscuits greedily
    for hunger in hunger_level:
        # Skip biscuits that are too small
        while biscuit_index < len(biscuit_size) and biscuit_size[biscuit_index] < hunger:
            biscuit_index += 1

        # If there’s still a biscuit available, feed the dog
        if biscuit_index < len(biscuit_size):
            satisfied_dogs += 1
            biscuit_index += 1  # Move to the next biscuit

    return satisfied_dogs
