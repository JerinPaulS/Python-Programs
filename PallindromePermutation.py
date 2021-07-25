'''
266. Pallindrome Permutation
Description
Given a string, determine if a permutation of the string could form a palindrome.

Example
Example1

Input: s = "code"
Output: False
Explanation: 
No solution
Example2

Input: s = "aab"
Output: True
Explanation: 
"aab" --> "aba"
Example3

Input: s = "carerac"
Output: True
Explanation: 
"carerac" --> "carerac"
'''
import collections
class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # write your code here
		char_freq = collections.Counter(s)
		count = 0
		for value in char_freq.values():
			count = count + (value % 2)
		if count > 1:
			return False
		else:
			return True

obj = Solution()
print(obj.canPermutePalindrome("code"))
print(obj.canPermutePalindrome("aab"))
print(obj.canPermutePalindrome("carerac"))