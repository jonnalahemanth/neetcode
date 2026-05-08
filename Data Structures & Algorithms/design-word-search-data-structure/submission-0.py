class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
        
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            for i in range(j, len(word)):
                ch = word[i]

                if ch == '.':
                    for child in node.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if ch not in node.children:
                        return False

                    node = node.children[ch]
                
            return node.is_end

        return dfs(0, self.root)
