'''
1668. Maximum Repeating Substring
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.

 

Example 1:

Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".
Example 2:

Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".
Example 3:

Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc". 
 

Constraints:

1 <= sequence.length <= 100
1 <= word.length <= 100
sequence and word contains only lowercase English letters.
'''
class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        count = 0
        resword = ''
        while True:
            resword = resword + word
            val = sequence.find(resword)
            if val == -1:
                break
            else:
                count = count + 1
        return count

obj = Solution()
print(obj.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba","aaaba"))

'''
		size = len(sequence)
        target = len(word)

        ptr1 = 0
        ptr2 = 0
        result = 0
        while ptr1 < size:
        	temp = ptr1
        	while ptr2 < target and temp < size and sequence[temp] == word[ptr2]:
        		temp = temp + 1
        		ptr2 = ptr2 + 1
        	if temp - 1 < size and target == ptr2 and sequence[temp - 1] == word[ptr2 - 1]:
        		result = result + 1
        		ptr1 = temp
        	else:
        		ptr1 = ptr1 + 1
        	ptr2 = 0

        return result
'''