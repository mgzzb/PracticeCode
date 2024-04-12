class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        def search_in_node(word, node):
            for i, char in enumerate(word):
                if char == '.':
                    # If the current character is '.', check all possible nodes at this position
                    for child in node.children.values():
                        if search_in_node(word[i+1:], child):
                            return True
                    return False
                else:
                    # Move to the corresponding child node
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.is_end_of_word
        
        return search_in_node(word, self.root)   


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
