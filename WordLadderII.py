'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 1000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
'''
from collections import deque
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        pattern_dict = {}
        wordList.append(beginWord)
        for word in wordList:
        	for i in range(len(word)):
        		pattern = word[:i] + "*" + word[i + 1:]
        		if pattern_dict.has_key(pattern):
        			pattern_dict[pattern].append(word)
        		else:
        			temp = []
        			temp.append(word)
        			pattern_dict[pattern] = temp

        qu = deque([beginWord])
        visited = set([beginWord])
        result = []
        temp = []
        count = 0



obj = Solution()
print(obj.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))

'''
		while qu:
        	for elemets in range(len(qu)):
	        	current = qu.popleft()
	        	if current == endWord:
	        		result.append(current)
	        		return result
	        	for i in range(len(current)):
	        		pattern = current[:i] + "*" + current[i + 1:]
	        		for word in pattern_dict[pattern]:
	        			if word not in visited:
	        				qu.append(word)
	        				visited.add(word)
        	result.append(current)
        return result

'''

'''
		wildcard_dict = collections.defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                w = word[:i] + '*' + word[i + 1:]                
                wildcard_dict[w].append(word)          
		
        queue = collections.deque([("", []), (beginWord, [beginWord])])
        visited = set()
        result = []
        tempVisited = set()
        while queue:            
            word, path = queue.pop()
            if not word:
                visited = visited.union(tempVisited)
                tempVisited = set()
                if len(queue):
                    queue.appendleft(("", []))                
                continue
            if word == endWord:                
                result.append(path[:])                
                continue               
            for i in range(len(word)):
                wild = word[:i] + '*' + word[i + 1:]
                for w in wildcard_dict[wild]:
                    if w not in visited:                        
                        tempVisited.add(w)
                        path.append(w)
                        queue.appendleft((w, path[:]))
                        path.pop()
                        
        return result
'''