import math
import os


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        if endWord not in wordList:
            return 0
        wordList = [beginWord] + sorted(list(set(wordList) - set([beginWord])))
        n = len(wordList)

        graph = self.to_graph(wordList)
        dist = [0] + [math.inf for _ in range(n-1)]
        prev = [None for _ in range(n)]
        bfs_queue, visited = [0], set([0])
        while len(bfs_queue) > 0:
            cursor = bfs_queue.pop(0)
            for neighbor, is_connected in enumerate(graph[cursor]):
                alt = dist[cursor] + 1
                if is_connected:
                    if alt < dist[neighbor]:
                        dist[neighbor] = alt
                        prev[neighbor] = cursor
                    if neighbor not in visited:
                        bfs_queue.append(neighbor)
                        visited.add(neighbor)
        return dist[wordList.index(endWord)] + 1 if dist[wordList.index(endWord)] != math.inf else 0

    def to_graph(self, wordlist):
        n = len(wordlist)
        graph = \
            [
                [1 for i in range(n)]
                for j in range(n)
            ]
        for i in range(n):
            for j in range(n):
                diff_count = 0
                for a, b in zip(wordlist[i], wordlist[j]):
                    if a != b:
                        diff_count += 1
                    if diff_count > 1:
                        graph[i][j] = 0
        return graph


assert Solution().ladderLength(
    "leet",
    "code",
    wordList=["lest", "leet", "lose", "code", "lode", "robe", "lost"]
) == 6
assert Solution().ladderLength(
    "a", "c",
    wordList=["a", "b", "c"]
) == 2
print(
    Solution().ladderLength(
        "hit", "cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"]
    )
)
print(
    Solution().ladderLength(
        "hot", "dog", wordList=["hot", "dog"])
)
print(
    Solution().ladderLength("hit", "cog",
                            wordList=["hot", "cog", "dot", "dog", "hit", "lot", "log"])
)
