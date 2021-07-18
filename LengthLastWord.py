'''
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Example 2:

Input: s = " "
Output: 0
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
       	list_str = s.split()
        if len(list_str) > 0 and list_str[-1].isalpha():        	
        	return(len(list_str[-1]))
        else:
        	return(0)        	

obj = Solution()
print(obj.lengthOfLastWord("Hello World"))
print(obj.lengthOfLastWord("     "))
print(obj.lengthOfLastWord("Hello t"))
print(obj.lengthOfLastWord("Hello "))