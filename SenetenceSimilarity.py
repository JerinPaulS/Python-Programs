'''

'''
class Solution(object):
	def areSentencesSimilar(self, words1, words2, pairs):
		"""
		:type words1: List[str]
		:type words2: List[str]
		:type pairs: List[List[str]]
		:rtype: bool
		"""
		if len(words1) != len(words2):
			return False

		for index in range(len(words1)):
			if words1[index] != words2[index]:
				if [words1[index], words2[index]] != pairs[index] and [words2[index], words1[index]] != pairs[index]:
					return False
		return True

obj = Solution()
print(obj.areSentencesSimilar(["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]))
print(obj.areSentencesSimilar(["great"], ["great"], []))
print(obj.areSentencesSimilar(["great"], ["doublepass", "good"], ["doublepass", "good"]))