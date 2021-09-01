'''
5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        max_len = 0

        for index in range(len(s)):
        	left = index
        	right = index

        	while left >= 0 and right < len(s) and s[left] == s[right]:
        		if right - left + 1 > max_len:
        			result = s[left:right + 1]
        			max_len = right - left + 1
        		left = left - 1
        		right = right + 1

        	left = index
        	right = index + 1

        	while left >= 0 and right < len(s) and s[left] == s[right]:
        		if right - left + 1 > max_len:
        			result = s[left:right + 1]
        			max_len = right - left + 1
        		left = left - 1
        		right = right + 1
        return result