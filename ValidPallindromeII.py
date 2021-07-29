'''
680. Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
'''
from collections import Counter
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        while start <= end:
        	if s[start] != s[end]:
        		return self.checkSubString(s, start + 1, end) or self.checkSubString(s, start, end - 1)
        	else:
	        	start = start + 1
	        	end = end - 1
        return True

    def checkSubString(self, s, start, end):
    	while start <= end:
    		if s[start] != s[end]:
    			return False
    		start = start + 1
    		end = end - 1

    	return True

obj = Solution()
print(obj.validPalindrome("aba"))
print(obj.validPalindrome("abca"))
print(obj.validPalindrome("cbbcc"))
print(obj.validPalindrome("tebbem"))
#"tebbem"