def max_independent_set(nums):
    if not nums:
        return []  # If the input list is empty, return an empty list
    n = len(nums)
    dp = [0] * (n + 1)
    dp[1] = max(0, nums[0])  # Initialize the dynamic programming table
    # Perform dynamic programming to find the maximum sum subsequence
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + max(nums[i - 1], 0))
    # Reconstruct the subsequence
    subsequence = []
    i = n
    while i > 0:
        if dp[i] == dp[i - 1]:
            i -= 1
        else:
            subsequence.append(nums[i - 1])
            i -= 2
    # If the maximum independent set is empty and 0 is present in the original set, return [0]
    if not subsequence and 0 in nums:
        return [0]
    return subsequence[::-1]