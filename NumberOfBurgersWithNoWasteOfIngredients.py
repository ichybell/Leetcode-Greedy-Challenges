"""
Number of Burgers with No Waste of Ingredients

Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:

Jumbo Burger: 4 tomato slices and 1 cheese slice.
Small Burger: 2 tomato slices and 1 cheese slice.
Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and the number of remaining cheeseSlices equal to 0. If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].

Example 1:

Input: tomatoSlices = 16, cheeseSlices = 7
Output: [1,6]
Explanation: To make one jumbo burger and 6 small burgers we need 4*1+2*6 = 16 tomato slices and 1*1+1*6 = 7 cheese slices.

Example 2:

Input: tomatoSlices = 17, cheeseSlices = 4
Output: []
Explanation: There are no total number of jumbo and small burgers that will get the remaining tomatoSlices equal to 0 and remaining cheeseSlices equal to 0.

Example 3:

Input: tomatoSlices = 4, cheeseSlices = 17
Output: []
Explanation: There are no total number of jumbo and small burgers that will get the remaining tomatoSlices equal to 0 and remaining cheeseSlices equal to 0.

Constraints:

0 <= tomatoSlices <= 10^7
0 <= cheeseSlices <= 10^7
"""

# Solution:
# We can use a greedy approach to solve this problem.
# We will first check if it is possible to make the remaining tomatoSlices equal to 0.
# If it is not possible return [].
# Then we will check if we can make the remaining cheeseSlices equal to 0 by adding jumbo burgers.
# If we can't make the remaining cheeseSlices equal to 0, we will add small burgers.

# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 == 1:
            return []
        jumbo_burgers = tomatoSlices // 2 - cheeseSlices
        small_burgers = cheeseSlices - jumbo_burgers
        if jumbo_burgers < 0 or small_burgers < 0:
            return []
        return [jumbo_burgers, small_burgers]
