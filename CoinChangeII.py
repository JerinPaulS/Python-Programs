'''
518. Coin Change 2
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
 

Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
'''
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for index in range(len(coins) - 1, -1, -1):
            newDP = [0] * (amount + 1)
            newDP[0] = 1
            
            for amt in range(1, amount + 1):
                newDP[amt] = dp[amt]
                if amt - coins[index] >= 0:
                    newDP[amt] = newDP[amt] + newDP[amt - coins[index]]
            dp = newDP
        return dp[amount]
        
        '''
        #Recursive Solution
        dp = {}

        def dfs(index, total):
        	if amount == total:
        		return 1
        	if index >= len(coins):
        		return 0
        	if total > amount:
        		return 0

        	if (index, total) in dp:
        		return dp[(index, total)]

        	dp[(index, total)] = dfs(index + 1, total) + dfs(index, total + coins[index])
        	return dp[(index, total)]

        return dfs(0, 0)
        '''