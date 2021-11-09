'''
1178. Number of Valid Words for Each Puzzle
With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
word contains the first letter of puzzle.
For each letter in word, that letter is in puzzle.
For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage", while
invalid words are "beefed" (does not include 'a') and "based" (includes 's' which is not in the puzzle).
Return an array answer, where answer[i] is the number of words in the given word list words that is valid with respect to the puzzle puzzles[i].
 

Example 1:

Input: words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation: 
1 valid word for "aboveyz" : "aaaa" 
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There are no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.
Example 2:

Input: words = ["apple","pleas","please"], puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
Output: [0,1,3,2,0]
 

Constraints:

1 <= words.length <= 105
4 <= words[i].length <= 50
1 <= puzzles.length <= 104
puzzles[i].length == 7
words[i] and puzzles[i] consist of lowercase English letters.
Each puzzles[i] does not contain repeated characters.
'''
import collections
class Solution:
    def findNumOfValidWords(self, words, puzzles):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        puzzle_dict = {}
        words_dict = {}
        alpha_dict = collections.defaultdict(list)

        for word in puzzles:
        	temp = ["0"] * 26
        	for char in alpha:
        		if char in word:
        			temp[ord(char) % 97] = "1"
        	puzzle_dict[word] = temp

        for word in words:
        	temp = ["0"] * 26
        	for char in alpha:
        		if char in word:
        			temp[ord(char) % 97] = "1"
        	words_dict[word] = temp

        for word in words:
        	for char in alpha:
        		if char in word:
        			alpha_dict[char].append(word)

        #print puzzle_dict
        #print words_dict
        #print alpha_dict

        result = []
        for puzzle in puzzles:
        	candidates = alpha_dict[puzzle[0]]
        	#print puzzle, candidates
        	count = 0
        	p_mask = int("".join(puzzle_dict[puzzle][::-1]))
        	for candidate in candidates:        		
        		w_mask = int("".join(words_dict[candidate][::-1]))
        		if p_mask & w_mask == w_mask:        			
        			print p_mask, w_mask, candidate
        			count += 1
        	result.append(count)

        return result

obj = Solution()
print(obj.findNumOfValidWords(["aaaa","asas","able","ability","actt","actor","access"], ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))


'''
		freq = defaultdict(int)
        for word in words: 
            mask = 0
            for c in word: mask |= 1 << (ord(c) - 97)
            freq[mask] += 1
            
        ans = []
        for puzzle in puzzles: 
            mask = val = 0 
            for c in puzzle: mask |= 1 << (ord(c) - 97)
            mask0 = mask # loop through sub-masks
            while mask: 
                if mask & (1 << ord(puzzle[0])-97): val += freq[mask]
                mask = mask0 & (mask - 1)
            ans.append(val)
        return ans
'''