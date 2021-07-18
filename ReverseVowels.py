'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''
class Solution(object):
	def reverseVowels(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		s = list(s)
		start = 0
		end = len(s) - 1
		vowels = "aeiouAEIOU"
		while start <= end:
			if s[start] in vowels and s[end] in vowels:
				temp = s[end]
				s[end] = s[start]
				s[start] = temp
				start = start + 1
				end = end - 1
			if start < len(s) and s[start] not in vowels:
				start = start + 1
			if end >=0 and s[end] not in vowels:
				end = end - 1
		return ''.join(s)

obj = Solution()
print(obj.reverseVowels("a."))
print(obj.reverseVowels(".a"))
#print(obj.reverseVowels("heoll"))
#print(obj.reverseVowels("leetcoed"))