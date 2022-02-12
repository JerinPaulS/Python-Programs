'''
127. Word Ladder
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neighbor = collections.defaultdict(list)
        
        for word in wordList:
            for index in range(len(word)):
                pattern = word[:index] + "*" + word[index + 1:]
                neighbor[pattern].append(word)
                
        visit = set([beginWord])
        queue = deque([beginWord])
        result = 1
        
        while len(queue) > 0:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result
                for index in range(len(word)):
                    pattern = word[:index] + "*" + word[index + 1:]
                    for neiWord in neighbor[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            queue.append(neiWord)
            result += 1
        return 0
        