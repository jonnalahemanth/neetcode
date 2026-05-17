from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        if beginWord == endWord:
            return 0

        word_set = set(wordList)

        q = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        while q:
            current_word, level = q.popleft()

            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c==current_word[i]:
                        continue

                    next_word = current_word[:i] + c + current_word[i+1:]

                    if next_word == endWord:
                        return level+1

                    if next_word in word_set and next_word not in visited:
                        q.append((next_word, level+1))
                        visited.add(next_word)

        return 0