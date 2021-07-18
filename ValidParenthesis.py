'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        flag = 0
        for element in s:
        	if element == '(' or element == '{'or element == '[':
        		stack.append(element)
        	elif element == ')':
        		if stack != [] and stack[-1] == '(':
        			stack.pop()
        		else:
        			flag = 1
        			break
        	elif element == '}':
        		if stack != [] and stack[-1] == '{':
        			stack.pop()
        		else:
        			flag = 1
        			break
        	elif element == ']':
        		if stack != [] and stack[-1] == '[':
        			stack.pop()
        		else:
        			flag = 1
        			break

        if flag == 1:
        	print("False")

        if stack == []:
        	print("True")
        else:
        	print("False")

obj = Solution()
obj.isValid("]")