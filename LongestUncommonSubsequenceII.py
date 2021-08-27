'''
Longest Uncommon Subsequence II
Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).
 

Example 1:

Input: strs = ["aba","cdc","eae"]
Output: 3
Example 2:

Input: strs = ["aaa","aaa","aa"]
Output: -1
 

Constraints:

1 <= strs.length <= 50
1 <= strs[i].length <= 10
strs[i] consists of lowercase English letters.
'''
import collections
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def isSubseq(a, b):
            j = 0
            for i in range(len(b)):
                if a[j] == b[i]:
                    j = j + 1
                    if j == len(a):
                        return True
            return False
        word_freq = collections.Counter(strs)
        sorted_words = sorted(word_freq.keys(), key = len, reverse = True)
        for i in range(len(sorted_words)):
            if word_freq[sorted_words[i]] > 1:
                continue
            if i == 0 or not any(isSubseq(sorted_words[i], sorted_words[j]) for j in range(i)):
                return len(sorted_words[i])
        return -1

obj = Solution()
print(obj.findLUSlength(["aba","cdc","eae"]))        