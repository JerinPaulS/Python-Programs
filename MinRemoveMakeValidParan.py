'''
1249. Minimum Remove to Make Valid Parentheses
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
'''
class Solution:
    def minRemoveToMakeValid(self, s):
        stack = []
        count = 0
        for char in s:
        	if char == "(":
        		stack.append("(")
        	elif char == ")" and len(stack) > 0 and stack[len(stack) - 1] == "(":
        		count += 1
        		stack.pop()
        result = ""
        stack = []
        tep_count = count
        for char in s:
        	if (char == "(" or char == ")"):
        		if char == "(" and count > 0:
        			stack.append("(")
        			result += char
        			count -= 1
        		elif char == ")" and tep_count > 0:
        			if len(stack) > 0:
        				stack.pop()
        				result += char
        				tep_count -= 1
        	elif char != "(" and char != ")":
        		result += char

        return result

obj = Solution()
print(obj.minRemoveToMakeValid("(a(b(c)d)"))