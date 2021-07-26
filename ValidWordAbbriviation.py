'''
408. Valid Word Abbreviation
Description
Given a non-empty string word and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Where 1 means one character is omitted, 2 means two characters are omitted, and so on.
Notice that only the above abbreviations are valid abbreviations of the string word. Any other string is not a valid abbreviation of word.

Example
Example 1:

Input : s = "internationalization", abbr = "i12iz4n"
Output : true
Example 2:

Input : s = "apple", abbr = "a2e"
Output : false
'''
class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        # write your code here
		ptr1 = 0
		ptr2 = 0
		count = ""
		while ptr1 < len(word) and ptr2 < len(abbr):
			if word[ptr1] == abbr[ptr2]:
				ptr1 = ptr1 + 1
				ptr2 = ptr2 + 1
			else:
				if abbr[ptr2].isalpha():
					return False
				else:
					while ptr2 < len(abbr) and abbr[ptr2].isdigit():
						count = count + abbr[ptr2]
						ptr2 = ptr2 + 1
					temp_count = int(count)
					count = ""
					ptr1 = ptr1 + temp_count
		if ptr1 == len(word) and ptr2 == len(abbr):
			return True
		else:
			return False

obj = Solution()
print(obj.validWordAbbreviation("internationalization", "i12iz4n"))
print(obj.validWordAbbreviation("apple", "a2e"))
print(obj.validWordAbbreviation("word", "w1rd"))