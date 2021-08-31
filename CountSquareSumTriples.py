'''
1925. Count Square Sum Triples
A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

 

Example 1:

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).
Example 2:

Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
 

Constraints:

1 <= n <= 250
'''
class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_set = set()

        for val in range(1, n + 1):
        	square_set.add(val * val)

        comb = itertools.combinations(square_set, 2)
        result = 0
        for c in comb:
        	if (c[0] + c[1]) in square_set:
        		result = result + 1
        return result * 2