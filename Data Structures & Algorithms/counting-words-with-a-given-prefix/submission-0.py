class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class BuildTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.end = True

    
    def search_prefix(self, pre):
        node = self.root

        for ch in pre:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # trie = BuildTrie()
        # count = 0
        # for word in words:
        #     trie.insert(word)

        # for word in words:
        #     if trie.search_prefix(pref):
        #         count += 1

        # return count

        count = 0

        for word in words:
            if word.startswith(pref):
                count += 1

        return count
