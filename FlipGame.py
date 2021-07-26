'''
293. Flip Game
Description
You are playing the following Flip Game with your friend: Given a string that contains only two characters: + and -, you can flip two consecutive "++" into "--", you can only flip one time. Please find all strings that can be obtained after one flip.

Write a program to find all possible states of the string after one valid move.

Example
Example1

Input:  s = "++++"
Output: 
[
  "--++",
  "+--+",
  "++--"
]
Example2

Input: s = "---+++-+++-+"
Output: 
[
	"---+++-+---+",
	"---+++---+-+",
	"---+---+++-+",
	"-----+-+++-+"
]
'''
class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
		possibleStates = []
		for index in range(len(s) - 1):
			temp = list(s)
			if s[index] == s[index + 1] and s[index] == "+":
				temp[index] = "-"
				temp[index + 1] = "-"
				possibleStates.append(''.join(temp))
		return possibleStates

obj = Solution()
print(obj.generatePossibleNextMoves("++++"))
print(obj.generatePossibleNextMoves("---+++-+++-+"))