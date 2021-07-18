'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", s = "dog dog dog dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lower-case English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
'''
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        word_dict = {}
        lett_dict = {}
        words = s.split()
        if len(words) != len(pattern):
        	return False
        for letter, word in zip(pattern, words):
        	if lett_dict.has_key(word):
        		if lett_dict[word] != letter:
        			return False
        	else:
        		lett_dict[word] = letter
        	if word_dict.has_key(letter):
        		if word_dict[letter] != word:
        			return False
        	else:
        		word_dict[letter] = word
        return True