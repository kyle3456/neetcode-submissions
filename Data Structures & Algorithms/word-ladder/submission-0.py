class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        possible = defaultdict(list)
        n = len(beginWord)
        wordList.append(beginWord)
        for original in wordList:
            for mutation in wordList:
                count = 0
                for i in range(n):
                    if original[i] != mutation[i]:
                        count += 1
                    if count == 2:
                        break
                if count == 1:
                    possible[original].append(mutation)

        q = deque()
        q.append((beginWord, 1))
        visited = {beginWord}

        while q:
            for i in range(len(q)):
                word, count = q.popleft()

                if word == endWord:
                    return count
                #cat, bat, bag
                possible_words = possible[word]

                for curr in possible_words:
                    if curr not in visited:
                        q.append((curr, count + 1))
                        visited.add(curr)

        return 0