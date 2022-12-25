"""
Jump Game II

Problem Description

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

## Example

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""


# Solution

# To solve this problem, we can use a greedy approach.

# We start by keeping track of the maximum index that we can reach at each step. 
# If the maximum index is greater than or equal to the last index, we return the number of jumps needed.

# To update the maximum index, we can simply take the maximum of the current maximum index and the current index plus the maximum jump length at the current index.

# This solution has a time complexity of O(n) and a space complexity of O(1).


## Code
class Solution:
    def jump(self, nums: List[int]) -> int:
        max_index = 0
        jumps = 0
        for i, jump in enumerate(nums):
            if max_index >= len(nums) - 1:
                return jumps
            max_index = max(max_index, i + jump)
            if i == max_index:
                return -1
            if i == jumps:
                jumps += 1
        return jumps
