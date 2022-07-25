import collections
from typing import List

'''
1. BFS 優於 DFS(總進出queue的數量較低，可能跟測試資料的特性有關係，
   DFS會time out的原因應該是他有個情境是[[0,1],[0,1],[0,1],[0,1],...]，
   用深度會炸好幾個order的量出來)，所以這類的題型要優先以廣度為考量
2. python內建的deque光是基本的append跟popleft效能就比list快不少
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        queue = collections.deque([])
        m, n = len(mat), len(mat[0])
        dist_mat = [[float('inf')]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    dist_mat[i][j] = 0

        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        while len(queue) > 0:
            count += 1
            i, j = queue.popleft()

            for d_i, d_j in neighbors:
                n_i, n_j = i + d_i, j + d_j
                if 0 <= n_i < m and 0 <= n_j < n and mat[n_i][n_j] == 1:
                    if dist_mat[i][j] + 1 < dist_mat[n_i][n_j]:
                        dist_mat[n_i][n_j] = dist_mat[i][j] + 1
                        queue.append((n_i, n_j))


        return dist_mat