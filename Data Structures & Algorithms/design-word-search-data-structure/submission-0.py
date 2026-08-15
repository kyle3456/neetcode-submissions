class TrieNode:
    def __init__(self):
        self.IsEnd = False
        self.Children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for character in word:
            if character not in curr.Children:
                curr.Children[character] = TrieNode()
    
            curr = curr.Children[character]
        
        curr.IsEnd = True

    def search(self, word: str) -> bool:
        def dfs(curr, index):
            if len(word) == index:
                return curr.IsEnd

            if word[index] == ".":
                for child in curr.Children.values():
                    if dfs(child, index + 1):
                        return True
            else:
                if word[index] not in curr.Children:
                    return False
                if dfs(curr.Children[word[index]], index + 1):
                    return True

            return False

        return dfs(self.root, 0)



        


    #b..n   {a, o}
    #ban
    #born