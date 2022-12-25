"""
Can Place Flowers

You have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.

"""

# Solution:
# We use a greedy approach to solve this problem.
# We iterate through the flowerbed array and check if the current element is 0 and the previous and next element are also 0.
# If this condition is satisfied, we plant a flower and increment the count of planted flowers.
# If the count of planted flowers is greater than or equal to n, we return True.
# If we reach the end of the array and the count of planted flowers is less than n, we return False.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
            if count >= n:
                return True
        return False