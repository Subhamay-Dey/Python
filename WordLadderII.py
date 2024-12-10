from collections import defaultdict, deque
from typing import List

def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    if endWord not in wordList:
        return []
    
    wordList = set(wordList)  # Convert to a set for faster lookups
    graph = defaultdict(list)
    length = len(beginWord)
    result = []
    found = False
    queue = deque([beginWord])
    visited = set([beginWord])
    local_visited = set()

    # Preprocess words to create patterns
    for word in wordList:
        for i in range(length):
            pattern = word[:i] + '*' + word[i + 1:]
            graph[pattern].append(word)

    # BFS to build the shortest path tree
    while queue and not found:
        local_visited.clear()
        for _ in range(len(queue)):
            current_word = queue.popleft()
            for i in range(length):
                pattern = current_word[:i] + '*' + current_word[i + 1:]
                for neighbor in graph[pattern]:
                    if neighbor == endWord:
                        found = True
                    if neighbor not in visited:
                        local_visited.add(neighbor)
                        queue.append(neighbor)
        visited.update(local_visited)

    # Backtrack to find all paths
    def backtrack(path):
        if path[-1] == beginWord:
            result.append(path[::-1])
            return
        for prev in path_tree[path[-1]]:
            backtrack(path + [prev])

    path_tree = defaultdict(list)
    for word in local_visited:
        for i in range(length):
            pattern = word[:i] + '*' + word[i + 1:]
            for neighbor in graph[pattern]:
                if neighbor in visited:
                    path_tree[word].append(neighbor)

    backtrack([endWord])
    return result

# Test the function
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(findLadders(beginWord, endWord, wordList))
