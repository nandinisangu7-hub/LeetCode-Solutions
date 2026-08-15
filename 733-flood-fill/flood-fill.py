class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or image[i][j]!=org:
                return
            image[i][j]=color
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        r=len(image)
        c=len(image[0])
        org=image[sr][sc]
        if image[sr][sc]==color:
            return image
        dfs(sr,sc)
        return image
        