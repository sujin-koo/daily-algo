'''
https://leetcode.com/problems/maximal-square/
'''

## refined version
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Constraints guarantee that matrix has at least one row and one column
        # (1 <= m, n <= 300), so an empty-check is optional here.
        # if not matrix or not matrix[0]:
        #    return 0

        row = len(matrix)
        col = len(matrix[0])

        # dp[r][c]: side length of the largest square
        # whose bottom-right corner is at (r, c)
        dp = [[int(matrix[r][c]) for c in range(col)] for r in range(row)]

        # Directions: left, up, top-left diagonal
        dr = [0, -1, -1]
        dc = [-1, 0, -1]

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == '1':
                    # Initialize minimum for the current cell
                    minimum = float("inf")

                    # Cells in the first row or first column
                    # cannot form a square larger than 1
                    if r == 0 or c == 0:
                        continue

                    # Take the minimum among left, up, and diagonal neighbors
                    for i in range(3):
                        prev_r = r + dr[i]
                        prev_c = c + dc[i]
                        # Boundary checks are unnecessary due to
                        # the first-row/first-column condition above
                        minimum = min(minimum, dp[prev_r][prev_c])

                    # Extend the square by 1
                    dp[r][c] = minimum + 1

        # The answer is the area of the largest square found
        maximum = max(max(row) for row in dp)
        return maximum * maximum
      

## -----------------------------
## first naive version

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        row = len(matrix)
        col = len(matrix[0])
        dp = [[0]*col for i in range(row)]
        
        for r in range(row):
            for c in range(col):
                dp[r][c] = int(matrix[r][c])

        dr = [0, -1, -1]
        dc = [-1, 0, -1]

        minimum = float("inf")
        for r in range(row): #0, 1, 2, 3
            for c in range(col): #0, 1, 2, 3, 4

                if matrix[r][c]=='1':
                    for i in range(3):
                        prev_r = r + dr[i]
                        prev_c = c + dc[i]
                        if 0<=prev_r<row and 0<=prev_c<col:
                            if dp[prev_r][prev_c] == 0:
                                minimum = float("inf")
                                break
                            minimum = min(minimum, dp[prev_r][prev_c])
                        else:
                            minimum = float("inf") 
                            break
                    if minimum != 0 and minimum !=float("inf") :
                        dp[r][c] = minimum + 1
                        minimum = float("inf")
                
        maximum = 0
        for r in range(row):
            for c in range(col):
                maximum = max(maximum, dp[r][c])

        return maximum * maximum
