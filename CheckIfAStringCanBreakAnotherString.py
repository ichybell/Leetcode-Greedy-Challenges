"""
Brief description of the problem:
Check If a String Can Break Another String problem is a problem where given two strings s1 and s2, we have to determine 
if s1 can be rearranged to form s2 or if s2 can be rearranged to form s1.
"""

# The solution implemented using a greedy approach:
# The solution implemented here is a greedy approach where we iterate over the characters of the strings and count the 
# frequency of each character. We then compare the frequency of each character in both strings. If the frequency of a 
# character in one string is greater than the other, we return False as it is not possible to rearrange the strings to 
# form each other. If the frequency of all characters is the same in both strings, we return True as it is possible to 
# rearrange the strings to form each other.

# Time complexity: O(n) where n is the number of characters in the strings. 
# Space complexity: O(1) as we only use a single integer to store the count of characters.

def checkIfCanBreak(s1: str, s2: str) -> bool:
    # count the frequency of each character in s1
    s1_count = [s1.count(ch) for ch in set(s1)]
    # count the frequency of each character in s2
    s2_count = [s2.count(ch) for ch in set(s2)]
    # compare the frequency of each character in both strings
    for count1, count2 in zip(sorted(s1_count), sorted(s2_count)):
        if count1 > count2:
            return False
    return True
