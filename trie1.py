class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def isValidPrefix(self, word):
        node = self.root
        for char in word:
            if char not in node.children or not node.children[char].isEnd:
                return False
            node = node.children[char]
        return True

def longestWord(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    longest = ""
    
    for word in words:
        if trie.isValidPrefix(word):
            if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                longest = word
    
    return longest
