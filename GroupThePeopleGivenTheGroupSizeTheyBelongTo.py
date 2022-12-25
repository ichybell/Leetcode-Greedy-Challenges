"""
Group the People Given the Group Size They Belong To

There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.

You can return the answer in any order. It is guaranteed that there exists at least one solution.

Example 1:

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

Example 2:

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]

Constraints:

groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n
"""

# Solution:
# We can use a greedy approach to solve this problem.
# We will create a dictionary to keep track of groups of each size.
# For each person, we will add them to the group of their size in the dictionary.
# If the group is not present in the dictionary, we will create a new group and add the person to the group.
# If the group is present and the size of the group is equal to the size, we will create a new group and add the person to the group.
# Otherwise, we will add the person to the existing group.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        result = []
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size not in groups:
                groups[size] = [i]
            else:
                if len(groups[size]) == size:
                    result.append(groups[size])
                    groups[size] = [i]
                else:
                    groups[size].append(i)
        for group in groups.values():
            result.append(group)
        return result
