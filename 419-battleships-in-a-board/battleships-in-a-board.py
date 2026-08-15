class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or board[i][j]!='X':
                return
            board[i][j]='.'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        r=len(board)
        c=len(board[0])
        count = 0
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'X':
                    count += 1
                    dfs(i, j)  
        return count
        