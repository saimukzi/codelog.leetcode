from typing import List
import collections
import math

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ret = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m-2):
            for j in range(n-2):
                x = 0
                x += grid[i][j]
                x += grid[i][j+1]
                x += grid[i][j+2]
                x += grid[i+1][j+1]
                x += grid[i+2][j]
                x += grid[i+2][j+1]
                x += grid[i+2][j+2]
                ret = max(ret, x)
        return ret
