'''
Stone Game
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 

Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
 

Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
'''
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """ 
        rows = len(piles)
        dp = []
        total_score = sum(piles)
        for row in range(rows):
        	temp = []
        	for index in range(rows):
        		temp.append(0)
        	dp.append(temp)

        loop = 0
        while loop < rows:
        	i = 0
        	j = loop
        	while j < rows:
        		if i == j:
        			dp[i][j] = piles[i]
        		elif j == i + 1:
        			dp[i][j] = max(piles[i], piles[j])
        		else:
        			score1 = piles[i] + min(dp[i + 1][j - 1], dp[i + 2][j])
        			score2 = piles[j] + min(dp[i + 1][j - 1], dp[i][j - 2])
        			dp[i][j] = max(score1, score2)
        		i = i + 1
        		j = j + 1
        	loop = loop + 1

        return total_score - dp[0][rows - 1] < dp[0][rows - 1]


obj = Solution()
print(obj.stoneGame([5,3,4,5]))
print(obj.stoneGame([8,9,7,6,7,6]))
'''
[[5, 5, 5, 5], 
 [0, 3, 4, 5], 
 [0, 0, 4, 5], 
 [0, 0, 0, 5]]


        for row in range(rows):
        	dp[row][row] = piles[row]

        for row in range(rows):
        	for col in range(row, rows):
        		if col == row + 1:
        			dp[row][col] = max(piles[row], piles[col])
'''