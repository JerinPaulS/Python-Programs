'''
Basic Calculator
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation.
'-' could be used as a unary operation but it has to be inside parentheses.
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
'''
class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		def calc(a, op, b):
			if op == "-":
				return a - b
			else:
				return a + b

		stack = []
		s = s.replace(" ", "")
		temp = "0"
		num = 0
		flag = 0
		if s[-1] != ")":
			s = s + " "
		sign = "+"
		for char in s:
			if char == "+" or char == "-" or char == ")" or char == "(" or char == " ":
				if flag == 1:
					num = calc(num, sign, int(temp))
				else:
					num = int(temp)
				temp = "0"
				flag = 1
			else:
				temp = temp + char
			if char == "+" or char == "-":
				sign = char
			if char == "(":
				stack.append(num)
				stack.append(sign)
				num = 0
				flag = 0
			if char == ")":
				if len(stack) > 1:
					s = stack.pop(len(stack) - 1)
					a = stack.pop(len(stack) - 1)
					num = calc(a, s, num)
		return num


obj = Solution()
print(obj.calculate("1 + 1"))
print(obj.calculate("(1+(4+5+2))-(3+(6+8))"))
print(obj.calculate("(1+(4+5+2)-3)+(6+8)"))