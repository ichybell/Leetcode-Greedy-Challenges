"""
A brief description of the problem:
Construct K Palindrome Strings problem is a problem where given a string s and an integer k, we have to determine if it is
possible to construct k palindromes using all the characters of s.
"""

# The solution implemented using a greedy approach:
# The solution implemented here is a greedy approach where we iterate over the characters of the string and count the number 
# of odd frequency characters. We then check if k is greater than or equal to the number of odd frequency characters. If it 
# is, we return True as we can form k palindromes using the odd frequency characters. If k is less than the number of odd 
# frequency characters, we check if k is even. If it is even, we return True as we can form k palindromes using the even 
# frequency characters. If k is odd, we return False as we cannot form k palindromes using the even frequency characters.

# Time complexity: O(n) where n is the number of characters in the string. 
# Space complexity: O(1) as we only use a single integer to store the count of odd frequency characters.

def canConstruct(s: str, k: int) -> bool:
    # count the number of odd frequency characters
    odd_count = sum([s.count(ch) % 2 for ch in set(s)])
    # check if k is greater than or equal to the number of odd frequency characters
    if k >= odd_count:
        return True
    # check if k is even
    if k % 2 == 0:
        return True
    return False
