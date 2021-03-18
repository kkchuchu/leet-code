import math
import os


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        if endWord not in wordList:
            return 0
        wordList = [beginWord] + list(set(wordList) - set([beginWord]))
        
        n = len(wordList)
        graph = self.to_graph(wordList)
        dist =[0] + [math.inf for _ in range(n-1)]
        prev = [None for _ in range(n)]
        bfs_queue, visited = [0], set([0])
        while len(bfs_queue) > 0:
            next_cursor = bfs_queue.pop(0)
            for neighbor, is_visited in enumerate(graph[next_cursor]):
                if is_visited:
                    if neighbor not in visited:
                        bfs_queue.append(neighbor)
                        visited.add(neighbor)
                    alt = dist[next_cursor] + 1
                    if alt < dist[neighbor]:
                        dist[neighbor] = alt
                        prev[neighbor] = next_cursor
            
            # print(bfs_queue, dist, prev)
            
        return dist[wordList.index(endWord)] + 1 if dist[wordList.index(endWord)] != math.inf else 0

    def to_graph(self, wordlist):
        n = len(wordlist)
        graph = \
            [
                [0 for i in range(n)]
                for j in range(n)
            ]
        for i in range(n):
            for j in range(n):
                if len(wordlist[i]) - len(list(set(wordlist[i]) & set(wordlist[j]))) == 1:
                    graph[i][j]= 1
        # print(*graph, sep="\n")
        return graph

print(Solution().ladderLength(
    "a", "c",
    wordList=["a","b","c"]
))
print(
    Solution().ladderLength(
        "hit", "cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"]
    )
)
print(
    Solution().ladderLength(
        "hot", "dog", wordList=["hot","dog"])
)
print(
    Solution().ladderLength("hit", "cog",
        wordList=["hot","cog","dot","dog","hit","lot","log"])
)
