class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(r, c, curr):
            if curr == len(word):
                return True
            elif r < 0 or r > ROWS - 1 or c < 0 or c > COLS -1 or board[r][c] != word[curr] or board[r][c] == "#":
                return False
            else:
                board[r][c] = "#"
                res = (dfs(r + 1, c, curr + 1) or dfs(r - 1, c, curr + 1) or 
                dfs(r, c + 1, curr + 1) or dfs(r, c - 1, curr + 1))
                board[r][c] = word[curr]
                return res
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True

        return False
