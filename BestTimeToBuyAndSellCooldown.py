'''
309. Best Time to Buy and Sell Stock with Cooldown
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = {}

        def dfs(index, buying):
        	if index >= len(prices):
        		return 0
        	if (index, buying) in dp:
        		return dp[(index, buying)]

        	cooldown = dfs(index + 1, buying)
        	if buying:
        		buy = dfs(index + 1, not buying) - prices[index]
        		dp[(index, buying)] = max(buy, cooldown)
        	else:
        		sell = dfs(index + 2, not buying) + prices[index]
        		dp[(index, buying)] = max(sell, cooldown)
        	return dp[(index, buying)]

        return dfs(0, True)