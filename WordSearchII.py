'''
212. Word Search II
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
'''
class TrieNode(object):
	def __init__(self):
		self.children = {}
		self.isWord = False

	def addWord(self, word):
		curr = self
		for char in word:
			if char not in curr.children:
				curr.children[char] = TrieNode()
			curr = curr.children[char]
		curr.isWord = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        for word in words:
        	root.addWord(word)
        rows, cols = len(board), len(board[0])
        visited = set()
        result = set()

        def dfs(row, col, node, word):
        	if row < 0 or col < 0 or row >= rows or col >= cols or (row, col) in visited or board[row][col] not in node.children:
        		return

        	visited.add((row, col))
        	node = node.children[board[row][col]]
        	word = word + board[row][col]
        	if node.isWord:
        		result.add(word)
        	dfs(row + 1, col, node, word)
        	dfs(row - 1, col, node, word)
        	dfs(row, col + 1, node, word)
        	dfs(row, col - 1, node, word)
        	visited.remove((row, col))
        	return

        for row in range(rows):
        	for col in range(cols):
        		dfs(row, col, root, "")
        return list(result)