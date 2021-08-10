'''
953. Verifying an Alien Dictionary
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_hash = {}

        order_len = len(order)
        for index in range(order_len):
        	order_hash[order[index]] = index

        rows = len(words)

        for row in range(rows - 1):
        	w1 = words[row]
        	w2 = words[row + 1]
        	size = len(w1)
        	upperbound = len(w2)
        	for index in range(size):
        		if index == upperbound:
        			return False
        		if w1[index] != w2[index]:
        			if order_hash[w2[index]] < order_hash[w1[index]]:
        				return False
        			break
    	return True

obj = Solution()
print(obj.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))
print(obj.isAlienSorted(["wor","woz","wow"], "worldabcefghijkmnpqstuvxyz"))
print(obj.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))