'''
243. Shortest Word Distance
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words= ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = "coding", word2 = "practice"
Output: 3

Input: word1 = "makes", word2 = "coding"
Output: 1

Note:
You may assume that word1 does not equal to word2 and word1 and word2 are both in the list.
'''

class Solution(object):
	def shortestDistance(self, words, word1, word2):
		"""
		:type words: list
		:type word1: str
		:type word2: str
        :rtype: int
		"""
		word_dict = {}
		for index in range(len(words)):
			if word_dict.has_key(words[index]):
				word_dict[words[index]].append(index)
			else:
				temp = [index]
				word_dict[words[index]] = temp

		temp_list1 = word_dict[str(word1)]
		temp_list2 = word_dict[word2]
		result = len(words)
		for i in temp_list1:
			for j in temp_list2:
				result = min(abs(i - j), result)
		return result

obj = Solution()
print(obj.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))
print(obj.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"))