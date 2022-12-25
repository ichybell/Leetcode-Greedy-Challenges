"""
Reduce Array Size to The Half

Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half.

Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.

Example 3:

Input: arr = [1,9]
Output: 1
Explanation: You have to remove 1.

Example 4:

Input: arr = [1000,1000,3,7]
Output: 1
Explanation: You have to remove 3 and 7 to make the new array [1000,1000] which is equal to half of the size of the old array.

Example 5:

Input: arr = [1,2,3,4,5,6,7,8,9,10]
Output: 5

Constraints:

1 <= arr.length <= 10^5
arr.length is even.
1 <= arr[i] <= 10^5
"""

# Solution:
# We can use a greedy approach to solve this problem.
# We can keep a dictionary to store the frequency of elements in the array.
# We can sort the dictionary by values in descending order and start adding the values to a set until we reach the half of the size of the array.

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = Counter(arr)
        s = sorted(d.values(), reverse=True)
        total = 0
        count = 0
        for i in s:
            total += i
            count += 1
            if total >= len(arr)//2:
                return count
        return count
