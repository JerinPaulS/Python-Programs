'''
1025. Divisor Game
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.

 

Example 1:

Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 

Constraints:

1 <= n <= 1000

'''
import math
class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [-1] * (n + 1)

        def helper(num):
        	if num == 1:
        		return False
        	if dp[num] != -1:
        		return dp[num]
        	else:
        		for val in range(1, int(math.sqrt(num)) + 1):
        			if num % val == 0:
        				calc = helper(num - val)
        				if calc == False:
        					dp[num] = True
        					return True
        		dp[num] = False
        		return False

        return helper(n)

obj = Solution()
print(obj.divisorGame(2))        