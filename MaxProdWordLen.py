'''
Maximum Product of Word Lengths

Solution
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

 

Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
 

Constraints:

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.
'''
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        Result = []
        for word in words:
        	temp = [0] * 26
        	for chars in word:
        		temp[ord(chars) % 97] = 1
        	Result.append(temp)

        prod = 0
        mamx_prod = 0

        for i in range(0, len(words) - 1):
        	for j in range(i + 1, len(words)):
        		flag = 0
        		for k in range(0, 26):

        			if Result[i][k] + Result[j][k] > 1:
        				flag = 1
        				break

        		if flag == 0:
	        		prod = len(words[i]) * len(words[j])
	        		if prod > mamx_prod:
	        			mamx_prod = prod

        print(mamx_prod)


import time
start = time.time()
obj = Solution()
obj.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
obj.maxProduct(["a","ab","abc","d","cd","bcd","abcd"])
obj.maxProduct(["a","aa","aaa","aaaa"])
end = time.time()
print("Runtime of the program is: " + str((end - start) * 1000) + "ms")