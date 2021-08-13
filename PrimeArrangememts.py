'''
1175. Prime Arrangements
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:

Input: n = 100
Output: 682289015
 

Constraints:

1 <= n <= 100
'''
import math
class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = (10 ** 9) + 7
        prime_nos = [0] * (n + 1)

        for val in range(2, int(math.sqrt(n)) + 1):
        	if prime_nos[val] == 0:
        		for index in range(val ** 2, n + 1, val):
        			prime_nos[index] = 1

        prim_comp = [0, 0]

        for index in range(2, n + 1):
        	if prime_nos[index] == 0:
        		prim_comp[0] = prim_comp[0] + 1
        prim_comp[1] = n - prim_comp[0]

        print prim_comp

        return (math.factorial(prim_comp[0]) * math.factorial(prim_comp[1])) % mod


obj = Solution()
print(obj.numPrimeArrangements(100))        