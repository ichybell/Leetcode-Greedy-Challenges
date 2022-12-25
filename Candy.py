"""
Candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.

"""

# Solution:
# We use two arrays l2r and r2l to keep track of the number of candies a child should get
# based on the rating of their neighbors.
# l2r[i] represents the number of candies that the ith child should get based on the ratings of their left neighbors.
# r2l[i] represents the number of candies that the ith child should get based on the ratings of their right neighbors.
# We can then update the value of the ith child by taking the maximum of l2r[i] and r2l[i].
# Finally we return the sum of the values in the array candies.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        n = len(ratings)
        l2r = [1] * n
        r2l = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                l2r[i] = l2r[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                r2l[i] = r2l[i+1] + 1
        candies = [max(l2r[i], r2l[i]) for i in range(n)]
        return sum(candies)
