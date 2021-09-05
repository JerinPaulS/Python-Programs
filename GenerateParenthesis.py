'''
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        temp = []
        result = []

        def Backtrack(open_count, closed_count):
        	if open_count == closed_count and open_count == n:
        		result.append("".join(temp))
        		return

        	if open_count < n:
        		temp.append("(")
        		Backtrack(open_count + 1, closed_count)
        		temp.pop()

        	if closed_count < open_count:
        		temp.append(")")
        		Backtrack(open_count, closed_count + 1)
        		temp.pop()

        Backtrack(0, 0)
       	return result