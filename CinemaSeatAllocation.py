"""
Cinema Seat Allocation

A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown below:

1 1 1 1 1 1 1 1 1 1 
2 2 2 2 2 2 2 2 2 2 
3 3 3 3 3 3 3 3 3 3 
...
n n n n n n n n n n 

You want to reserve a contiguous block of empty seats, r rows high and c seats wide.

Return the number of ways you can reserve a block of empty seats.

Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: n = 2, m = 3, r = 1, c = 2
Output: 6
Explanation: The following blocks are all available to be reserved:
[1,2], [1,3], [1,4], [2,2], [2,3], [2,4]

Example 2:

Input: n = 2, m = 2, r = 2, c = 1
Output: 0
Explanation: Because there is no way to reserve 2 rows 1 wide there are no valid blocks.

Example 3:

Input: n = 3, m = 5, r = 2, c = 2
Output: 10

Constraints:

1 <= n <= 10^9
1 <= m <= 10^9
1 <= r <= n
1 <= c <= m
"""

# Solution:
# We can use a greedy approach to solve this problem.
# We can take the first row that is not fully booked, then if there are enough seats we can add to the count and move to the next row.
# If there are not enough seats, we can check if we can get enough seats in the next row.
# If we can't we return 0.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxNumberOfFamilies(n: int, reservedSeats: List[List[int]]) -> int:
        # initialize a list of n zeros
        seats = [0] * n
        
        # mark the occupied seats
        for r, c in reservedSeats:
            seats[r-1] |= 1 << c-1
        
        # initialize the answer
        ans = 0
        
        # iterate over the seats
        for r in seats:
            # check if the group of friends can sit together
            if r & 0b111111000 == 0:
                ans += 2
            # check if the group of friends can sit together
            elif r & 0b111110000 == 0 or r & 0b111100000 == 0:
                ans += 1
        # return the answer
        return ans
