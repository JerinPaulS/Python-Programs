'''
187. Repeated DNA Sequences
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.
'''
import collections
class Solution:
    def findRepeatedDnaSequences(self, s):
        word_dict = collections.defaultdict(int)
        result = []
        if len(s) < 10:
        	return result

        for index in range(len(s) - 10 + 1):
        	word_dict[s[index:index + 10]] += 1

        for key in word_dict:
        	if word_dict[key] > 1:
        		result.append(key)

        return result

obj = Solution()
print(obj.findRepeatedDnaSequences("AAAAAAAAAAA"))        