'''
Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
'''
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
        	return 0
        prime_result = [1] * n
        prime_result[0] = 0
        prime_result[1] = 0
        for val in range(2, int(math.ceil(math.sqrt(n))) + 1):
        	if prime_result[val] == 1:
        		for index in range(val ** 2, n, val):
        			prime_result[index] = 0
        return sum(prime_result)

obj = Solution()
#print(obj.countPrimes(10))
print(obj.countPrimes(7))
#print(obj.countPrimes(1))