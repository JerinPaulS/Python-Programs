'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0


Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
        	return(0)
        if len(haystack) < len(needle):
        	return(-1)
        i = 0
        j = 0
        while i < len(haystack):
        	if haystack[i] == needle[j]:
        		temp = i
        		while temp < len(haystack) and j < len(needle):
        			if haystack[temp] != needle[j]:
        				j = 0
        				break
        			elif haystack[temp] == needle[j]:
        				j = j + 1
        				temp = temp + 1
        	i = i + 1
	        if j == len(needle):
	        	return(temp - j)
        return(-1)

obj = Solution()
print(obj.strStr("hello", "ll"))
print(obj.strStr("aaaaa", "bba"))
print(obj.strStr("", ""))
print(obj.strStr("mississippi","issip"))