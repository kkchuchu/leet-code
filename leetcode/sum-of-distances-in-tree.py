from collections import defaultdict
from typing import Optional


class Solution:
    def sumOfDistancesInTree(self, N: int, edges):
        neighbors = {i: [] for i in range(N)}
        for edge in edges:
            s, e = edge[0], edge[1]
            neighbors[s].append(e)
            neighbors[e].append(s)
        visited, level = set([]), 0
        bfs_queue = [(0, level)]
        point2level_parent = {
            i: {
                "level": 0, "parent": set([]), "child": set([])
            }
            for i in range(N)
        }
        while len(bfs_queue) > 0:
            (cursor, level) = bfs_queue.pop(0)
            point2level_parent[cursor]["level"] = level
            visited.add(cursor)
            for neighbor in neighbors[cursor]:
                point2level_parent[cursor]["child"].add(neighbor)
                point2level_parent[neighbor]["parent"].add(cursor)
                if neighbor not in visited:
                    bfs_queue.append((neighbor, level+1))
        
        result = []
        for i in range(N):    
            i_level = levels[i]
            r = 0
            for point, level in levels.items():
                if i == point:
                    continue
                elif level == i_level:
                    r += 2
                else:
                    r += level - i_level if level > i_level else i_level - level
            result.append(r)
        return result

        
    def slow_sumOfDistancesInTree(self, N: int, edges):
        graph = [[0 for _ in range(N)] for _ in range(N)]
        for edge in edges:
            start, end = edge[0], edge[1]
            graph[start][end] = 1
            graph[end][start] = 1
            pass

        graphs = [graph]
        for ith_connected in range(N):
            r = self.mat_mul(graphs[ith_connected], graph)
            
            graphs.append(r)


        for i in range(N):
            for j in range(N):
                graph[i][j] = min(
                    [graphs[length][i][j] for length in range(len(graphs)) if graphs[length][i][j] > 0] or [0]
                )
            
        
        result = [
            sum([a for j, a in enumerate(graph[i]) if j != i]) for i in range(N)
        ]
        return result
    
    def mat_mul(self, a, b):
        m, n = len(a), len(b[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                for k in range(len(b)):
                    if a[i][k] * b[k][j] > 0:
                        result[i][j] += a[i][k] + b[k][j]
                    else:
                        result[i][j] += 0
        return result
                
assert Solution().sumOfDistancesInTree(
    N=6,
    edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
) == [8, 12, 6, 10, 10, 10]

assert Solution().sumOfDistancesInTree(
    N=1,
    edges=[]
) == [0]

assert Solution().sumOfDistancesInTree(
    N=100,
    edges=[[74,34],[67,44],[81,40],[1,97],[44,88],[95,23],[77,78],[67,29],[98,1],[89,3],[60,91],[30,28],[64,85],[47,72],[64,9],[26,35],[24,1],[43,35],[62,86],[92,86],[59,89],[31,3],[31,92],[1,33],[54,68],[57,63],[2,3],[36,64],[6,9],[3,67],[99,70],[9,47],[45,16],[94,92],[22,9],[56,31],[89,84],[40,31],[37,38],[57,52],[75,76],[1,26],[65,79],[5,39],[96,47],[55,14],[83,54],[6,32],[11,26],[8,40],[32,69],[32,14],[78,79],[34,92],[31,75],[39,45],[3,79],[71,31],[82,74],[51,58],[27,35],[60,70],[31,51],[53,74],[64,60],[84,90],[39,40],[28,80],[0,47],[31,41],[1,25],[56,48],[93,10],[1,17],[37,7],[47,15],[49,41],[5,18],[4,92],[25,64],[84,95],[10,95],[63,66],[46,87],[92,50],[66,3],[64,75],[61,98],[78,12],[54,71],[7,65],[87,39],[73,96],[61,20],[64,19],[21,69],[30,6],[42,72],[13,67]]
)
