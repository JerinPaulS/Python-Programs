'''
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lps = [0] * len(s)
        for i in range(1, len(s)):
        	j = lps[i - 1]
        	while j > 0 and s[i] != s[j]:
        		j = lps[j - 1]
        	if s[i] == s[j]:
        		j = j + 1
        	lps[i] = j

        result = lps[len(s) - 1]
        if result != 0 and (result % (len(s) - result) == 0):
        	return True
        else:
        	return False
